package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// CSProblems ...
type CSProblems struct {
	set []*CS
}

// Solve ...
func (p *CSProblems) Solve() {
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

// CS ...
type CS struct {
	data   [][]int
	num    int
	output int
}

// CreateCS ...
func CreateCS() s.Problem {
	set := make([]*CS, 0, 4)

	set = append(set, &CS{
		data: [][]int{
			{1, 0},
		},
		num:    2,
		output: 1,
	})

	set = append(set, &CS{
		data: [][]int{
			{1, 0}, {0, 1},
		},
		num:    2,
		output: 0,
	})

	set = append(set, &CS{
		data: [][]int{
			{1, 0}, {2, 1}, {3, 1}, {3, 2}, {2, 0},
		},
		num:    4,
		output: 1,
	})

	set = append(set, &CS{
		data: [][]int{
			{1, 0}, {2, 1}, {3, 1}, {3, 2}, {2, 0}, {0, 3},
		},
		num:    4,
		output: 0,
	})

	return &CSProblems{set}
}

func (p *CS) solve() int {
	size := len(p.data)
	if size < p.num-1 {
		return 1
	}

	m := make(map[int][]int, p.num)
	visited := make([]int, p.num)

	for i := 0; i < size; i++ {
		dep, pre := p.data[i][0], p.data[i][1]
		m[pre] = append(m[pre], dep)
		visited[dep] = 1
	}

	start := []int{}
	for i := 0; i < p.num; i++ {
		if visited[i] == 0 {
			start = append(start, i)
		} else {
			visited[i] = 0
		}
	}

	if len(start) == 0 {
		return 0
	}

	var curr []int
	stack := make([][]int, 0, p.num)
	// chain := make([]int, 0, p.num)

	for i := 0; i < len(start); i++ {
		head := start[i]
		dep := m[head]

		if len(dep) == 0 {
			continue
		}

		stack = append(stack, dep)
		visited[head] = 1

		for len(stack) > 0 {
			tail := len(stack) - 1
			pop := true
			curr, stack = stack[tail], stack[:tail]

			for i := 0; i < len(curr); i++ {
				head = curr[i]
				if visited[head] == 1 {
					// found a circular dependency, abort
					return 0
				}

				dep = m[head]
				if len(dep) == 0 {
					continue
				}

				// push to the stack and go deeper into the next level
				visited[head] = 1
				curr = curr[i:]
				stack = append(stack, curr, dep)
				pop = false

				break
			}

			if pop && len(stack) > 0 {
				tail = len(stack) - 1
				visited[stack[tail][0]] = 0
				stack[tail] = stack[tail][1:]
			}
		}

		// not necessary, but for consistency
		visited[head] = 0
	}

	return 1
}
