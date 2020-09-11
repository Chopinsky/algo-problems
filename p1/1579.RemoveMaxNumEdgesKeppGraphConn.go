package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// RMNEKGCProblems ...
type RMNEKGCProblems struct {
	set []*RMNEKGC
}

// Solve ...
func (p *RMNEKGCProblems) Solve() {
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

// RMNEKGC ...
type RMNEKGC struct {
	data   [][]int
	n      int
	output int
}

// CreateRMNEKGC ...
func CreateRMNEKGC() s.Problem {
	set := make([]*RMNEKGC, 0, 4)

	set = append(set, &RMNEKGC{
		data: [][]int{
			{3, 1, 2},
			{3, 2, 3},
			{1, 1, 3},
			{1, 2, 4},
			{1, 1, 2},
			{2, 3, 4},
		},
		n:      4,
		output: 2,
	})

	set = append(set, &RMNEKGC{
		data: [][]int{
			{3, 1, 2},
			{3, 2, 3},
			{1, 1, 4},
			{2, 1, 4},
		},
		n:      4,
		output: 0,
	})

	set = append(set, &RMNEKGC{
		data: [][]int{
			{3, 2, 3},
			{1, 1, 2},
			{2, 3, 4},
		},
		n:      4,
		output: -1,
	})

	return &RMNEKGCProblems{set}
}

func (p *RMNEKGC) solve() int {
	n, g := p.n, p.data

	a := make([]int, n+1)
	b := make([]int, n+1)

	for i := 1; i <= n; i++ {
		a[i] = i
		b[i] = i
	}

	for i := range g {
		if g[i][0] == 1 {
			union(a, g[i][1], g[i][2])
		} else if g[i][0] == 2 {
			union(b, g[i][1], g[i][2])
		} else {
			union(a, g[i][1], g[i][2])
			union(b, g[i][1], g[i][2])
		}
	}

	abase, bbase := findRoot(a, 1), findRoot(b, 1)
	for i := 2; i <= n; i++ {
		if findRoot(a, i) != abase {
			return -1
		}

		if findRoot(b, i) != bbase {
			return -1
		}
	}

	return 0
}

func union(a []int, i, j int) {
	ri, rj := findRoot(a, i), findRoot(a, j)

	if ri < rj {
		a[rj] = ri
	} else {
		a[ri] = rj
	}
}

func findRoot(a []int, i int) int {
	for a[i] != i {
		i = a[i]
	}

	return i
}
