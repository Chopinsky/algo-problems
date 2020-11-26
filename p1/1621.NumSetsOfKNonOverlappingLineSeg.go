package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// NSOKNOLSProblems ...
type NSOKNOLSProblems struct {
	set []*NSOKNOLS
}

// Solve ...
func (p *NSOKNOLSProblems) Solve() {
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

// NSOKNOLS ...
type NSOKNOLS struct {
	n      int
	k      int
	output int
}

// CreateNSOKNOLS ...
func CreateNSOKNOLS() s.Problem {
	set := make([]*NSOKNOLS, 0, 4)

	set = append(set, &NSOKNOLS{
		n:      4,
		k:      2,
		output: 5,
	})

	set = append(set, &NSOKNOLS{
		n:      3,
		k:      1,
		output: 3,
	})

	set = append(set, &NSOKNOLS{
		n:      30,
		k:      7,
		output: 796297179,
	})

	set = append(set, &NSOKNOLS{
		n:      5,
		k:      3,
		output: 7,
	})

	set = append(set, &NSOKNOLS{
		n:      3,
		k:      2,
		output: 1,
	})

	return &NSOKNOLSProblems{set}
}

func (p *NSOKNOLS) solve() int {
	mod := 1000000007
	n, k := p.n, p.k

	dp := make([]int, n)
	prefix := make([]int, n)

	for i := range dp {
		if i > 0 {
			dp[i] = dp[i-1] + i
			prefix[i] = dp[i] + prefix[i-1]
		}
	}

	// fmt.Println(dp, prefix)

	for i := 2; i <= k; i++ {
		next := make([]int, n)
		np := make([]int, n)

		next[i] = 1
		np[i] = next[i]

		for j := i + 1; j < n; j++ {
			next[j] = next[j-1] + prefix[j-1]
			np[j] = next[j] + np[j-1]
		}

		dp = next
		prefix = np
	}

	return dp[n-1] % mod
}
