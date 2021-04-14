package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// GCWTProblems ...
type GCWTProblems struct {
	set []*GCWT
}

// Solve ...
func (p *GCWTProblems) Solve() {
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

// GCWT ...
type GCWT struct {
	data   [][]int
	n      int
	th     int
	output int
}

// CreateGCWT ...
func CreateGCWT() s.Problem {
	set := make([]*GCWT, 0, 4)

	set = append(set, &GCWT{
		data:   [][]int{{1, 4}, {2, 5}, {3, 6}},
		n:      6,
		th:     2,
		output: 0,
	})

	return &GCWTProblems{set}
}

func (p *GCWT) solve() int {
	return 0
}

func areConnected(n int, threshold int, queries [][]int) []bool {
	ans := make([]bool, len(queries))

	u := make([]int, n+1)
	for i := range u {
		u[i] = i
	}

	for i := threshold + 1; i*2 <= n; i++ {

		for j := 2; i*j <= n; j++ {
			if i != j && j > threshold {
				union(u, i, j)
			}

			union(u, i, i*j)
		}
	}

	for i, v := range queries {
		if v[0] <= threshold || v[1] <= threshold {
			continue
		}

		i0, i1 := findRoot(u, v[0]), findRoot(u, v[1])

		if i0 == i1 {
			ans[i] = true
		}
	}

	return ans
}
