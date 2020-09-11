package p0

import (
	"container/heap"
	"fmt"
	"time"

	s "go-problems/shared"
)

// NDTProblems ...
type NDTProblems struct {
	set []*NDT
}

// Solve ...
func (p *NDTProblems) Solve() {
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

// NDT ...
type NDT struct {
	data   [][]int
	n      int
	k      int
	output int
}

// CreateNDT ...
func CreateNDT() s.Problem {
	set := make([]*NDT, 0, 4)

	set = append(set, &NDT{
		data:   [][]int{},
		n:      4,
		k:      2,
		output: 0,
	})

	return &NDTProblems{set}
}

func (p *NDT) solve() int {
	return networkDelayTime(p.data, p.n, p.k)
}

func networkDelayTime(times [][]int, N int, K int) int {
	costs := make([]int, N+1)
	stack := make(pqn, 0, 2*N)
	routes := make(map[int][][]int)

	for _, t := range times {
		routes[t[0]] = append(routes[t[0]], t[1:])
	}

	// fmt.Println(routes)

	stack.Push([]int{K, 0})

	for stack.Len() > 0 {
		c := stack.Pop().([]int)

		// fmt.Println(c)

		if next, ok := routes[c[0]]; ok {
			for _, r := range next {
				node, cost := r[0], r[1]
				if node == K {
					continue
				}

				if costs[node] == 0 || c[1]+cost < costs[node] {
					costs[node] = c[1] + cost
					stack.Push([]int{node, costs[node]})
				}
			}
		}
	}

	best := 0
	fmt.Println(costs)

	for i, t := range costs {
		if i == K || i == 0 {
			continue
		}

		if t == 0 {
			return -1
		}

		if t > best {
			best = t
		}
	}

	return best
}

type pqn [][]int

func (h pqn) Len() int {
	return len(h)
}

func (h pqn) Less(i, j int) bool {
	return h[i][1] < h[j][1]
}

func (h pqn) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *pqn) Push(x interface{}) {
	v := x.([]int)
	*h = append(*h, v)
}

func (h *pqn) Pop() interface{} {
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
