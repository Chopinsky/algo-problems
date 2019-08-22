package problems

import (
	"fmt"
)

// SP ...
type SP struct {
	source [][]int
	output int
}

// CreateSP ...
func CreateSP() *SP {
	return &SP{}
}

// Build ...
func (p *SP) Build(test int) {
	switch test {
	case 1:
		p.source = [][]int{
			{1, 2, 3},
			{5, 4, 0},
		}
		p.output = -1

	case 2:
		p.source = [][]int{
			{4, 1, 2},
			{5, 0, 3},
		}
		p.output = 5

	default:
		p.source = [][]int{
			{1, 2, 3},
			{4, 0, 5},
		}
		p.output = 1

	}
}

// Run ...
func (p *SP) Run() {
	fmt.Println("Calculated results: ", p.walk())
	fmt.Println("Expected results: ", p.output)
}

func (p *SP) walk() int {
	visited := make(map[int]struct{})
	visited[hashKey(p.source)] = empty

	stack := []board{newBoard(p.source)}
	steps := 0

	for {
		if len(stack) == 0 {
			break
		}

		temp := []board{}
		steps++

		for _, next := range stack {
			slotX := next.pos[0]
			slotY := next.pos[1]

			for i := 0; i < 4; i++ {
				x := slotX + dir[i]
				y := slotY + dir[i+1]

				if x >= 0 && x <= 1 && y >= 0 && y <= 2 {
					cand := newBoard(next.b)

					// now swap and update the slot pos
					cand.b[slotX][slotY] = cand.b[x][y]
					cand.b[x][y] = 0

					key := hashKey(cand.b)
					if key == 142530 {
						return steps
					}

					if _, ok := visited[key]; !ok {
						cand.pos[0] = x
						cand.pos[1] = y
						temp = append(temp, cand)
					}
				}
			}

			visited[hashKey(next.b)] = empty
		}

		stack = temp
	}

	return -1
}

func hashKey(b [][]int) int {
	res := 0
	for i := 0; i < 3; i++ {
		res = res*10 + b[0][i]
		res = res*10 + b[1][i]
	}

	return res
}

type board struct {
	b   [][]int
	pos []int
}

func newBoard(src [][]int) board {
	pos := make([]int, 2)
	b := make([][]int, 2)

	for i := range src {
		b[i] = make([]int, 3)
		for j := range src[i] {
			b[i][j] = src[i][j]

			if b[i][j] == 0 {
				pos[0] = i
				pos[1] = j
			}
		}
	}

	return board{b, pos}
}
