package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MPLFSProblems ...
type MPLFSProblems struct {
	set []*MPLFS
}

// Solve ...
func (p *MPLFSProblems) Solve() {
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

// MPLFS ...
type MPLFS struct {
	a      string
	b      string
	output int
}

// CreateMPLFS ...
func CreateMPLFS() s.Problem {
	set := make([]*MPLFS, 0, 4)

	set = append(set, &MPLFS{
		a:      "cacb",
		b:      "cbba",
		output: 5,
	})

	set = append(set, &MPLFS{
		a:      "ab",
		b:      "ab",
		output: 3,
	})

	set = append(set, &MPLFS{
		a:      "aa",
		b:      "bb",
		output: 0,
	})

	return &MPLFSProblems{set}
}

func (p *MPLFS) solve() int {
	a, b := p.a, p.b
	dp := make([]int, len(b))
	next := make([]int, 0, len(b))

	for i := len(a) - 1; i >= 0; i-- {
		src := rune(a[i])

		for j, ch := range b {
			point := 0
			matched := false

			if src == ch {
				point = 2
				matched = true

				if i == len(a)-1 && j > 0 {
					point++
				}
			}

			if j == 0 {
				next = append(next, max(point, dp[j]))
			} else if !matched {
				next = append(next, max(next[j-1], dp[j]))
			} else {
				next = append(next, max(next[j-1], dp[j-1]+point))
			}
		}

		// fmt.Println(dp, next)

		dp, next = next, dp
		next = next[:0]
	}

	return dp[len(b)-1]
}
