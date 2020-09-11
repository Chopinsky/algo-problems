package p0

import (
	"container/heap"
	"fmt"
	"time"

	s "go-problems/shared"
)

// SRWProblems ...
type SRWProblems struct {
	set []*SRW
}

// Solve ...
func (p *SRWProblems) Solve() {
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

// SRW ...
type SRW struct {
	data   [][]int
	output int
}

// CreateSRW ...
func CreateSRW() s.Problem {
	set := make([]*SRW, 0, 4)

	set = append(set, &SRW{
		data: [][]int{
			{0, 1, 2, 3, 4},
			{24, 23, 22, 21, 5},
			{12, 13, 14, 15, 16},
			{11, 17, 18, 19, 20},
			{10, 9, 8, 7, 6},
		},
		output: 16,
	})

	return &SRWProblems{set}
}

func (p *SRW) solve() int {
	return swimInWater(p.data)
}

type stack [][]int

func (h stack) Len() int {
	return len(h)
}

func (h stack) Less(i, j int) bool {
	return h[i][2] < h[j][2]
}

func (h stack) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *stack) Push(x interface{}) {
	v := x.([]int)
	*h = append(*h, v)

	heap.Fix(h, h.Len()-1)
}

func (h *stack) Pop() interface{} {
	old := *h
	n := old.Len()
	v := old[0]

	if n > 1 {
		old.Swap(0, n-1)
		old[n-1] = nil
	}

	*h = old[:n-1]

	if n > 2 {
		heap.Fix(h, 0)
	}

	return v
}

func swimInWater(grid [][]int) int {
	h, w := len(grid), len(grid[0])
	dirs := []int{-1, 0, 1, 0, -1}

	visited := make([][]bool, h)
	for i := range visited {
		visited[i] = make([]bool, w)

		if i == 0 {
			visited[0][0] = true
		}
	}

	s := make(stack, 0, h*w)
	s.Push([]int{0, 0, grid[0][0]})

	max := grid[0][0]
	for s.Len() > 0 {
		next := s.Pop().([]int)
		x, y, cost := next[0], next[1], next[2]

		// fmt.Println(x, y)

		if cost > max {
			max = cost
		}

		if x == h-1 && y == w-1 {
			break
		}

		for i := 0; i < 4; i++ {
			x0, y0 := x+dirs[i], y+dirs[i+1]

			if x0 < 0 || x0 >= h || y0 < 0 || y0 >= w || visited[x0][y0] {
				continue
			}

			visited[x0][y0] = true
			s.Push([]int{x0, y0, grid[x0][y0]})
		}
	}

	return max
}

func swimInWater1(grid [][]int) int {
	h, w := len(grid), len(grid[0])
	dirs := []int{-1, 0, 1, 0, -1}

	visited := make([][]bool, h)
	for i := range visited {
		visited[i] = make([]bool, w)
		if i == 0 {
			visited[0][0] = true
		}
	}

	stack := make(map[int]int, h*w)
	stack[0] = 0

	t := grid[0][0]
	if expand(0, h, w, t, grid, stack, visited, dirs) {
		return t
	}

	minWait := 1
	done := false

	for !done {
		minWait = -1

		for k := range stack {
			x, y := fromKey(k, w)
			hasNext := false

			for i := 0; i < 4; i++ {
				x0, y0 := x+dirs[i], y+dirs[i+1]
				if x0 < 0 || x0 >= h || y0 < 0 || y0 >= w || visited[x0][y0] {
					continue
				}

				hasNext = true

				if grid[x0][y0] <= t {
					if x0 == h-1 && y0 == w-1 {
						done = true
						break
					}

					key := getKey(x0, y0, w)
					visited[x0][y0] = true
					stack[key] = t
					minWait = 1

					// todo: follow through (x0, y0)
					if expand(key, h, w, t, grid, stack, visited, dirs) {
						done = true
						break
					}
				} else if minWait == -1 || grid[x0][y0]-t < minWait {
					minWait = grid[x0][y0] - t
				}
			}

			if done {
				break
			}

			if !hasNext {
				delete(stack, k)
			}
		}

		if minWait == -1 {
			minWait = 1
		}

		// fmt.Println(t, minWait, stack)

		if !done {
			t += minWait
		}
	}

	return t
}

func expand(key, h, w, t int, grid [][]int, stack map[int]int, visited [][]bool, dirs []int) bool {
	var c int
	s := []int{key}

	for len(s) > 0 {
		c, s = s[0], s[1:]
		x, y := fromKey(c, w)

		for i := 0; i < 4; i++ {
			x0, y0 := x+dirs[i], y+dirs[i+1]
			if x0 < 0 || x0 >= h || y0 < 0 || y0 >= w || visited[x0][y0] || grid[x0][y0] > t {
				continue
			}

			if x0 == h-1 && y0 == w-1 {
				return true
			}

			k := getKey(x0, y0, w)

			stack[k] = t
			visited[x0][y0] = true

			s = append(s, k)
		}
	}

	return false
}

func fromKey(k, w int) (int, int) {
	return k / w, k % w
}
