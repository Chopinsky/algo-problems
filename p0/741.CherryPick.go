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
	forward bool
	path    map[int]bool
}

func (p *CP) solve() int {
	h, w, grid := len(p.data), len(p.data[0]), p.data
	scores := make([][][]int, h)

	for i := 0; i < h; i++ {
		scores[i] = make([][]int, w)

		for j := 0; j < w; j++ {
			scores[i][j] = make([]int, 2)
		}
	}

	stack := make([]seeker, 0, h*w)
	stack = append(stack, seeker{
		x:       0,
		y:       0,
		count:   grid[0][0],
		forward: true,
		path:    make(map[int]bool),
	})

	var curr seeker
	var cCount, max int

	for len(stack) > 0 {
		curr, stack = stack[0], stack[1:]
		x, y, forward, count, path := curr.x, curr.y, curr.forward, curr.count, curr.path

		if (forward && count < scores[x][y][0]) || (!forward && count < scores[x][y][1]) {
			// a better solution exists in the queue, stop this seeker.
			continue
		}

		if forward {
			if x+1 < h && grid[x+1][y] != -1 && count+grid[x+1][y] > scores[x+1][y][0] {
				next := seeker{
					x:       x + 1,
					y:       y,
					count:   count + grid[x+1][y],
					forward: true,
					path:    nextPath(path, x+1, y, w),
				}

				if next.x == h-1 && next.y == w-1 {
					next.forward = false
					// fmt.Println("x", count, path)
				}

				scores[x+1][y][0] = next.count
				stack = append(stack, next)
			}

			if y+1 < w && grid[x][y+1] != -1 && count+grid[x][y+1] > scores[x][y+1][0] {
				next := seeker{
					x:       x,
					y:       y + 1,
					count:   count + grid[x][y+1],
					forward: true,
					path:    nextPath(path, x, y+1, w),
				}

				if next.x == h-1 && next.y == w-1 {
					next.forward = false
					// fmt.Println("y", next.count, next.path)
				}

				scores[x][y+1][0] = next.count
				stack = append(stack, next)
			}
		} else {
			if x-1 >= 0 && grid[x-1][y] != -1 {
				key := calcKeys(x-1, y, w)

				if grid[x-1][y] >= 1 && !path[key] {
					cCount = 1
				} else {
					cCount = 0
				}

				if count+cCount > scores[x-1][y][1] {
					next := seeker{
						x:       x - 1,
						y:       y,
						count:   count + cCount,
						forward: false,
						path:    nextPath(path, x-1, y, w),
					}

					if next.x == 0 && next.y == 0 && next.count > max {
						max = next.count
					}

					scores[x-1][y][1] = next.count
					if next.x > 0 || next.y > 0 {
						stack = append(stack, next)
					}
				}
			}

			if y-1 >= 0 && grid[x][y-1] != -1 {
				key := calcKeys(x, y-1, w)

				if grid[x][y-1] >= 1 && !path[key] {
					cCount = 1
				} else {
					cCount = 0
				}

				if count+cCount > scores[x][y-1][1] {
					next := seeker{
						x:       x,
						y:       y - 1,
						count:   count + cCount,
						forward: false,
						path:    nextPath(path, x, y-1, w),
					}

					if next.x == 0 && next.y == 0 && next.count > max {
						max = next.count
					}

					scores[x][y-1][1] = next.count
					if next.x > 0 || next.y > 0 {
						stack = append(stack, next)
					}
				}
			}
		}
	}

	return max
}

func calcKeys(i, j, pad int) int {
	return i*pad + j
}

func nextPath(src map[int]bool, i, j, pad int) map[int]bool {
	nextp := make(map[int]bool)

	for k := range src {
		nextp[k] = true
	}

	key := calcKeys(i, j, pad)
	nextp[key] = true

	return nextp
}
