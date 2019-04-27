package problems

import (
	"fmt"
	"strconv"
)

// BFH ...
type BFH struct {
	grid   [][]int
	hits   [][]int
	output []int
}

// CreateBFH ...
func CreateBFH() *BFH {
	return &BFH{}
}

// Build ...
func (p *BFH) Build(test int) {
	switch test {
	case 1:
		p.grid = [][]int{
			{1, 0, 0, 0},
			{1, 1, 1, 0},
		}
		p.hits = [][]int{{1, 0}}
		p.output = []int{2}

	default:
		p.grid = [][]int{
			{1, 0, 0, 0},
			{1, 1, 0, 0},
		}
		p.hits = [][]int{{1, 1}, {1, 0}}
		p.output = []int{0, 0}

	}
}

// Run ...
func (p *BFH) Run() {
	sizeX := len(p.grid)
	sizeY := len(p.grid[0])
	falls := make([]int, len(p.hits))

	for i, coord := range p.hits {
		falls[i] = p.hit(coord, sizeX, sizeY)
	}

	fmt.Println("Calculated result: ", falls)
	fmt.Println("Expected result: ", p.output)
}

func (p *BFH) hit(brick []int, sizeX, sizeY int) int {
	count := 0
	p.grid[brick[0]][brick[1]] = 0

	for _, b := range p.getBricks(brick, sizeX, sizeY) {
		if p.grid[b[0]][b[1]] == 0 {
			continue
		}

		count += p.hitBrick(b, sizeX, sizeY)
	}

	return count
}

func (p *BFH) getBricks(source []int, sizeX, sizeY int) [][]int {
	bricks := [][]int{}

	var x, y int
	for i := 0; i < 4; i++ {
		x = source[0] + dir[i]
		y = source[1] + dir[i+1]

		// over the boundary, return
		if x < 1 || y < 0 || x > sizeX-1 || y > sizeY-1 || p.grid[x][y] == 0 {
			continue
		}

		bricks = append(bricks, []int{x, y})
	}

	return bricks
}

func (p *BFH) hitBrick(source []int, sizeX, sizeY int) int {
	count := 0
	visited := make(map[string][]int)
	stack := [][]int{source}

	var brick []int
	coord := make([]int, 2)

	for {
		if len(stack) == 0 {
			break
		}

		fmt.Println(stack)

		brick, stack = stack[0], stack[1:]
		visited[toString(brick)] = brick
		count++

		for i := 0; i < 4; i++ {
			coord[0] = brick[0] + dir[i]
			coord[1] = brick[1] + dir[i+1]

			// over the boundary, return
			if coord[0] < 0 || coord[1] < 0 || coord[0] > sizeX-1 || coord[1] > sizeY-1 || p.grid[coord[0]][coord[1]] == 0 {
				continue
			}

			// if the brick block is connected to a top brick, the whole structure holds
			if coord[0] == 0 && p.grid[coord[0]][coord[1]] == 1 {
				return 0
			}

			// add the brick to the stack
			if _, ok := visited[toString(coord)]; ok {
				continue
			}

			stack = append(stack, []int{coord[0], coord[1]})
		}

		fmt.Println(stack)
	}

	// the brick block will fall altogheter, update it now
	if count > 0 {
		for _, v := range visited {
			p.grid[v[0]][v[1]] = 0
		}
	}

	return count
}

func (p *BFH) canFall(x, y, srcX, srcY, sizeX, sizeY int) bool {
	// over the boundary, return
	if x < 1 || y < 0 || x > sizeX-1 || y > sizeY-1 {
		return false
	}

	// if already empty slot, return
	if p.grid[x][y] == 0 {
		return false
	}

	// find out if there's something to stick with
	var nX, nY int
	for i := 0; i < 4; i++ {
		nX = x + dir[i]
		nY = y + dir[i+1]

		if nX < 0 || nY < 0 || nX > sizeX-1 || nY > sizeY-1 {
			continue
		}

		if nX != srcX && nY != srcY && p.grid[nX][nY] == 1 {
			return false
		}
	}

	return true
}

func toString(coord []int) string {
	return strconv.Itoa(coord[0]) + "," + strconv.Itoa(coord[1])
}
