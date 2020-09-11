package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// LARProblems ...
type LARProblems struct {
	set []*LAR
}

// Solve ...
func (p *LARProblems) Solve() {
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

// LAR ...
type LAR struct {
	data   [][]int
	quiet  []int
	output []int
}

// CreateLAR ...
func CreateLAR() s.Problem {
	set := make([]*LAR, 0, 4)

	set = append(set, &LAR{
		data: [][]int{
			{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3},
		},
		quiet:  []int{3, 2, 5, 4, 6, 1, 7, 0},
		output: []int{5, 5, 2, 5, 4, 5, 6, 7},
	})

	return &LARProblems{set}
}

func (p *LAR) solve() []int {
	return loudAndRich(p.data, p.quiet)
}

func loudAndRich(richer [][]int, quiet []int) []int {
	size := len(quiet)

	nodes := make([]*larNode, size)
	ans := make([]int, size)

	for i := range ans {
		ans[i] = i
		nodes[i] = &larNode{
			inc: 0,
			out: []int{},
		}
	}

	for _, p := range richer {
		o, i := p[0], p[1]
		nodes[o].out = append(nodes[o].out, i)
		nodes[i].inc++
	}

	stack := make([]int, 0, size)
	for i := range nodes {
		// fmt.Println(nodes[i].inc, nodes[i].out)
		if nodes[i].inc == 0 {
			stack = append(stack, i)
		}
	}

	fmt.Println(stack)

	var curr *larNode
	var idx int

	for len(stack) > 0 {
		curr, idx, stack = nodes[stack[0]], stack[0], stack[1:]

		for _, p := range curr.out {
			nodes[p].inc--

			if nodes[p].inc == 0 {
				stack = append(stack, p)
			}

			if quiet[ans[idx]] < quiet[ans[p]] {
				ans[p] = ans[idx]
			}
		}
	}

	return ans
}

type larNode struct {
	inc int
	out []int
}
