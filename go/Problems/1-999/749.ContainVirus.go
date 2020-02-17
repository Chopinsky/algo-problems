package problems

import (
	"fmt"

	d "../../Utils"
)

// CV ...
type CV struct {
	source    [][]int
	output    int
	testCount int
}

// CreateCV ...
func CreateCV() *CV {
	return &CV{}
}

// Build ...
func (p *CV) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	switch test {
	default:
		p.source = [][]int{
			{0, 1, 0, 0, 0, 0, 0, 1},
			{0, 1, 0, 0, 0, 0, 0, 1},
			{0, 0, 0, 0, 0, 0, 0, 1},
			{0, 0, 0, 0, 0, 0, 0, 0},
		}
		p.output = 10

	}
}

// ResetGlobals ...
func (p *CV) ResetGlobals() {
}

// Run ...
func (p *CV) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(isolate(p.source), p.output)
			} else {
				isolate(p.source)
			}
		}
	}
}

func isolate(src [][]int) int {
	maps, groups := buildIslands(src)
	row, col := len(maps), len(maps[0])

	if d.DEBUG {
		/// Map lengends:
		///  -1        --> wall
		///   0        --> free zone
		///   N (N>0)  --> infection zone with zone number
		for i := range maps {
			fmt.Println(maps[i])
		}

		fmt.Println()
		fmt.Println(groups)
	}

	return isolateOne(maps, groups, row, col)
}

func isolateOne(maps [][]int, groups map[int][][]int, row, col int) int {
	bounds, idx := findBoundries(maps, groups, row, col)

	// no more walls to be built
	if len(bounds) == 0 || idx < 0 {
		return 0
	}

	if coords, ok := bounds[idx]; ok {
		// build the wall and update the maps/groups
		maps = buildWall(maps, coords)
		delete(bounds, idx)
		delete(groups, idx)

		// now spread infections
		maps, groups = spreadAndMerge(maps, groups, bounds, row)

		// recursive search aka dfs
		return len(coords) + isolateOne(maps, groups, row, col)
	}

	return 0
}

func findBoundries(maps [][]int, groups map[int][][]int, row, col int) (map[int][][]int, int) {
	counts := make(map[int][][]int, len(groups))
	maxIdx, maxVal := -1, -1

	for k, v := range groups {
		next := findOneBoundry(v, maps, row, col)
		size := len(next)

		if size > 0 {
			counts[k] = next
			if size > maxVal {
				maxIdx = k
				maxVal = size
			}
		}
	}

	return counts, maxIdx
}

func findOneBoundry(coords, maps [][]int, row, col int) [][]int {
	bounds := make([][]int, 0, 2*len(coords))

	var x, y int
	for i := range coords {
		x, y = coords[i][0], coords[i][1]

		if x > 0 && maps[x-1][y] == 0 {
			bounds = append(bounds, []int{x - 1, y})
		}

		if x < row-1 && maps[x+1][y] == 0 {
			bounds = append(bounds, []int{x + 1, y})
		}

		if y > 0 && maps[x][y-1] == 0 {
			bounds = append(bounds, []int{x, y - 1})
		}

		if y < col-1 && maps[x][y+1] == 0 {
			bounds = append(bounds, []int{x, y + 1})
		}
	}

	return bounds
}

func buildWall(maps, coords [][]int) [][]int {
	for i := range coords {
		maps[coords[i][0]][coords[i][1]] = -1
	}

	return maps
}

func spreadAndMerge(maps [][]int, groups, coords map[int][][]int, row int) ([][]int, map[int][][]int) {
	merge := make(map[int]int)

	var x, y, val int
	for k, v := range coords {
		for i := range v {
			x, y = v[i][0], v[i][1]
			val = maps[x][y]

			if val < 0 || k == val {
				// meets a wall or the area has already been marked, move on
				continue
			}

			if val > 0 {
				// the spot already belongs to a neightboring zone
				if k < val {
					merge[val] = k
				} else {
					merge[k] = val
				}
			} else {
				// only spread if the spot is a free-zone
				maps[x][y] = k
				groups[k] = append(groups[k], v[i])
			}
		}
	}

	return mergeZones(maps, groups, merge)
}

func mergeZones(maps [][]int, groups map[int][][]int, targets map[int]int) ([][]int, map[int][][]int) {
	var root int

	for k := range targets {
		root = findRootZone(targets, k)

		if coords, ok := groups[k]; ok {
			// update all zones to the root zone number
			for i := range coords {
				maps[coords[i][0]][coords[i][1]] = root
			}

			// update the group index
			groups[root] = append(groups[root], coords...)
			delete(groups, k)
		}
	}

	return maps, groups
}

func findRootZone(zones map[int]int, src int) int {
	for {
		if val, ok := zones[src]; ok {
			src = val
		} else {
			return src
		}
	}
}

func buildIslands(src [][]int) ([][]int, map[int][][]int) {
	row, col := len(src), len(src[0])
	base := make([]int, row*col+1)
	groups := make(map[int][][]int)

	for i := range base {
		base[i] = i
	}

	var key int
	for r := range src {
		for c := range src[r] {
			// flattern 2d to 1d key
			key = r*col + c + 1

			if src[r][c] == 1 {
				// the island
				if r > 0 && src[r-1][c] == 1 {
					// try connect with the island above
					base = union(base, (r-1)*col+c+1, key)
				} else if c > 0 && src[r][c-1] == 1 {
					// otherwise, try connect with the island to the left
					base = union(base, r*col+c, key)
				} else {
					// not connected, starting a new island number
					base[key] = key
				}
			} else {
				// the sea
				base[key] = 0
			}
		}
	}

	// reforming back to 2d map for later use
	islands := make([][]int, row)
	for i := range islands {
		islands[i] = make([]int, col)
		for j := range islands[i] {
			id := base[i*col+j+1]
			islands[i][j] = id

			if id > 0 {
				groups[id] = append(groups[id], []int{i, j})
			}
		}
	}

	return islands, groups
}

func union(base []int, src, tgt int) []int {
	base[tgt] = findID(base, src)
	return base
}

func findID(base []int, src int) int {
	if base[src] == src {
		// we've reached the base id, return the result
		return src
	}

	return findID(base, base[src])
}
