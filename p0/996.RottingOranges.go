package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// ROProblems ...
type ROProblems struct {
	set []*RO
}

// Solve ...
func (p *ROProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm finished in:", time.Since(start))
}

// RO ...
type RO struct {
	data   [][]int
	output int
}

// CreateRO ...
func CreateRO() s.Problem {
	set := make([]*RO, 0, 4)

	set = append(set, &RO{
		data: [][]int{
			{2, 1, 1}, {1, 1, 0}, {0, 1, 1},
		},
		output: 4,
	})

	set = append(set, &RO{
		data: [][]int{
			{2, 1, 1}, {0, 1, 1}, {1, 0, 1},
		},
		output: -1,
	})

	set = append(set, &RO{
		data: [][]int{
			{0, 2},
		},
		output: 0,
	})

	return &ROProblems{set}
}

func (p *RO) solve() int {
	return orangesRotting(p.data)
}

var dirs = []int{-1, 0, 1, 0, -1}

func orangesRotting(grid [][]int) int {
	if grid == nil || grid[0] == nil {
		return 0
	}

	h, w := len(grid), len(grid[0])
	q := make([]int, 0, h*w)
	temp := make([]int, 0, h*w)
	count, time := 0, 0

	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] == 1 {
				count++
			} else if grid[i][j] == 2 {
				q = append(q, getKey(i, j, w))
			}
		}
	}

	if count == 0 {
		return 0
	}

	if len(q) == 0 {
		return -1
	}

	for len(q) > 0 && count > 0 {
		time++

		for i := range q {
			x, y := getCoord(q[i], w)

			for j := 0; j < 4; j++ {
				x0, y0 := x+dirs[j], y+dirs[j+1]

				if x0 >= 0 && x0 < h && y0 >= 0 && y0 < w && grid[x0][y0] == 1 {
					grid[x0][y0] = 2
					count--
					temp = append(temp, getKey(x0, y0, w))
				}
			}
		}

		q = q[len(q):]
		q, temp = temp, q
	}

	if count > 0 {
		return -1
	}

	return time
}

func getKey(i, j, w int) int {
	return i*w + j
}

func getCoord(k, w int) (int, int) {
	return k / w, k % w
}
