package problems

import (
	"fmt"

	d "../../Utils"
)

// MMG ...
type MMG struct {
	source    [][]string
	output    int
	testCount int
}

// CreateMMG ...
func CreateMMG() *MMG {
	return &MMG{}
}

// Build ...
func (p *MMG) Build(test int) {
	switch test {
	case 1:
		p.source = [][]string{
			{"#", "#", "#", "#", "#", "#", "#"},
			{"#", "#", "#", "T", "#", "#", "#"},
			{"#", ".", ".", ".", "B", "S", "#"},
			{"#", ".", "#", ".", "#", "#", "#"},
			{"#", ".", ".", ".", "#", "#", "#"},
			{"#", "#", "#", "#", "#", "#", "#"},
		}
		p.output = 4

	default:
		p.source = [][]string{
			{"#", "#", "#", "#", "#", "#"},
			{"#", "T", "#", "#", "#", "#"},
			{"#", ".", ".", "B", ".", "#"},
			{"#", ".", "#", "#", ".", "#"},
			{"#", ".", ".", ".", "S", "#"},
			{"#", "#", "#", "#", "#", "#"},
		}
		p.output = 3

	}

	p.ResetGlobals()
	p.testCount = 2
}

// Run ...
func (p *MMG) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcMMG(p.source), p.output)
			} else {
				calcMMG(p.source)
			}
		}
	}
}

// ResetGlobals ...
func (p *MMG) ResetGlobals() {
}

func calcMMG(src [][]string) int {
	boxInDeadend, t, b, w := markFeatures(src)

	if boxInDeadend {
		return -1
	}

	if d.DEBUG {
		fmt.Println("target at: ", t.x, t.y)
		fmt.Println("box at: ", b.x, b.y)
		fmt.Println("worker at: ", w.x, w.y)

		fmt.Println()

		for _, row := range src {
			fmt.Println(row)
		}
	}

	stack := []*move{
		&move{
			box:    b,
			worker: w,
			visited: map[int]uint8{
				b.toKey(): 0,
			},
		},
	}

	steps := 0

	for len(stack) > 0 {
		temp := make([]*move, 0, 2*len(stack))

		for i := 0; i < len(stack); i++ {
			curr := stack[i]
			for _, nextPos := range nextBoxPos(curr.box, curr.worker, src, curr.visited) {
				if nextPos.x == t.x && nextPos.y == t.y {
					return steps + 1
				}

				temp = append(temp, curr.makeNext(nextPos))
			}
		}

		stack = temp
		steps++
	}

	return -1
}

type move struct {
	box     *pos
	worker  *pos
	visited map[int]uint8
}

func (m *move) makeNext(nextPos *pos) *move {
	visited := make(map[int]uint8)
	for k, v := range m.visited {
		visited[k] = v
	}

	visited[m.box.toKey()] = 1

	return &move{
		box:     nextPos,
		worker:  m.box,
		visited: visited,
	}
}

func workerToPos(start, final, box *pos, src [][]string) bool {
	if start.x == final.x && start.y == final.y {
		return true
	}

	stack := []*pos{start}
	var next *pos

	visited := make(map[int]struct{})

	for len(stack) > 0 {
		// moved to the next position
		next, stack = stack[0], stack[1:]
		visited[next.toKey()] = empty

		for i := 0; i < len(dir)-1; i++ {
			x0, y0 := next.x+dir[i], next.y+dir[i+1]
			if src[x0][y0] == "#" || (x0 == box.x && y0 == box.y) {
				continue
			}

			if x0 == final.x && y0 == final.y {
				return true
			}

			if _, ok := visited[toMapKey(x0, y0)]; ok {
				continue
			}

			stack = append(stack, newPos(x0, y0))
		}
	}

	return false
}

func nextBoxPos(box, worker *pos, src [][]string, visited map[int]uint8) []*pos {
	var res []*pos
	var x0, y0, xw, yw int

	for i := 0; i < len(dir)-1; i++ {
		x0, y0 = box.x+dir[i], box.y+dir[i+1]

		if src[x0][y0] == "." || src[x0][y0] == "+" || src[x0][y0] == "T" {
			if visited != nil {
				key := toMapKey(x0, y0)
				if count, ok := visited[key]; ok {
					if count > 1 {
						// if the position has been visited more than once, skip it
						continue
					}

					visited[key]++
				}
			}

			if x0 == box.x {
				xw = x0
				if y0 > box.y {
					yw = box.y - 1
				} else {
					yw = box.y + 1
				}
			} else {
				yw = y0
				if x0 > box.x {
					xw = box.x - 1
				} else {
					xw = box.x + 1
				}
			}

			if !workerToPos(worker, newPos(xw, yw), box, src) {
				continue
			}

			if res == nil {
				res = []*pos{newPos(x0, y0)}
			} else {
				res = append(res, newPos(x0, y0))
			}
		}
	}

	return res
}

type pos struct {
	x int
	y int
}

func toMapKey(x, y int) int {
	return x*256 + y
}

func (p *pos) toKey() int {
	return p.x*256 + p.y
}

func newPos(x, y int) *pos {
	return &pos{
		x: x,
		y: y,
	}
}

func markFeatures(srcMap [][]string) (bool, *pos, *pos, *pos) {
	var target, box, worker *pos
	var feature int

	boxInDeadend := false
	cache := make([]bool, 4)
	// deadends := make([]*pos, 0, 4)

	for i := 1; i < len(srcMap)-1; i++ {
		row := srcMap[i]
		for j := 1; j < len(srcMap[i])-1; j++ {
			switch row[j] {
			case "T":
				target = newPos(i, j)

			case "B":
				box = newPos(i, j)

			case "S":
				worker = newPos(i, j)
			}

			if row[j] != "T" && row[j] != "#" {
				feature = checkPositionFeature(i, j, srcMap, cache)
				if feature == 2 {
					// mark the crossroad
					srcMap[i][j] = "+"
				} else if feature == 1 {
					// mark the deadend
					if row[j] == "B" {
						// if the box is in deadend, just quit
						return true, target, box, worker
					}

					// otherwise, mark the location for later processing
					srcMap[i][j] = "D"
					// deadends = append(deadends, newPos(i, j))
				}
			}
		}
	}

	// if len(deadends) > 0 {
	// 	for _, p := range deadends {
	// 		expandDeadend(p, srcMap)
	// 	}
	// }

	return boxInDeadend, target, box, worker
}

func expandDeadend(start *pos, src [][]string) {
	stack := []*pos{start}
	var next *pos

	for len(stack) > 0 {
		next, stack = stack[0], stack[1:]

		for i := 0; i < len(dir)-1; i++ {
			x0, y0 := next.x+dir[i], next.y+dir[i+1]
			if src[x0][y0] == "." || src[x0][y0] == "S" {
				src[x0][y0] = "D"
				stack = append(stack, newPos(x0, y0))
			}
		}
	}
}

func checkPositionFeature(x, y int, src [][]string, cache []bool) int {
	count := 0

	for i := 0; i < len(dir)-1; i++ {
		x0, y0 := x+dir[i], y+dir[i+1]
		if src[x0][y0] != "#" {
			count++
			cache[i] = true
		} else {
			cache[i] = false
		}
	}

	if count > 2 {
		// 3 or 4, a crossroad
		return 2
	}

	if count < 2 {
		// 0 or 1, a deadend
		return 1
	}

	if (cache[0] && cache[1]) || (cache[1] && cache[2]) || (cache[2] && cache[3]) || (cache[3] && cache[0]) {
		// 2, and a corner -> hence a deadend
		return 1
	}

	// 2, and a straight pass
	return 0
}
