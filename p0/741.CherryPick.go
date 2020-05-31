package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// CPProblems ...
type CPProblems struct {
	set []*CP
}

// Solve ...
func (p *CPProblems) Solve() {
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

	fmt.Println("Algorithm took", time.Since(start))
}

// CP ...
type CP struct {
	data   [][]int
	output int
}

// CreateCP ...
func CreateCP() s.Problem {
	set := make([]*CP, 0, 4)

	set = append(set, &CP{
		data: [][]int{
			{0, 1, -1},
			{1, 0, -1},
			{1, 1, 1},
		},
		output: 5,
	})

	return &CPProblems{set}
}

type seeker struct {
	x       int
	y       int
	count   int
	id      int
	forward bool
}

var gID int

func (p *CP) solve() int {
	gID = 0
	h, w, grid := len(p.data), len(p.data[0]), p.data

	scores := make([][][]int, h)
	visited := make([][]map[int]bool, h)

	for i := 0; i < h; i++ {
		scores[i] = make([][]int, w)
		visited[i] = make([]map[int]bool, w)

		for j := 0; j < w; j++ {
			scores[i][j] = make([]int, 2)
		}
	}

	stack := make([]seeker, 0, h*w)
	stack = append(stack, seeker{
		x:       0,
		y:       0,
		count:   grid[0][0],
		id:      getID(),
		forward: true,
	})

	var curr seeker

	for len(stack) > 0 {
		curr, stack = stack[0], stack[1:]
		x, y, forward, count := curr.x, curr.y, curr.forward, curr.count

		if (forward && count < scores[x][y][0]) || (!forward && count < scores[x][y][1]) {
			// a better solution exists in the queue, stop this seeker.
			continue
		}

		if forward {
			if x+1 < h && grid[x+1][y] >= 0 && count+grid[x+1][y] > scores[x+1][y][0] {
				next := seeker{
					x:       x + 1,
					y:       y,
					count:   count + grid[x+1][y],
					id:      getID(),
					forward: true,
				}

				if next.x == h-1 && next.y == w-1 {
					next.forward = false
				}

				scores[x+1][y][0] = next.count
				visited[x+1][y][next.id] = true
				stack = append(stack, next)
			}

			if y+1 < w && grid[x][y+1] >= 0 && count+grid[x][y+1] > scores[x][y+1][0] {
				next := seeker{
					x:       x,
					y:       y + 1,
					count:   count + grid[x][y+1],
					id:      getID(),
					forward: true,
				}

				if next.x == h-1 && next.y == w-1 {
					next.forward = false
				}

				scores[x][y+1][0] = next.count
				visited[x][y+1][next.id] = true
				stack = append(stack, next)
			}
		} else {
			if x-1 >= 0 && grid[x-1][y] >= 0 {

			}

			if y-1 >= 0 && grid[x][y+1] >= 0 {

			}
		}
	}

	return 0
}

func calcKeys(i, j, pad int) int {
	return i*pad + j
}

func getID() int {
	gID++
	return gID
}
