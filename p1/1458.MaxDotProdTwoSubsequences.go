package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MDPTSProblems ...
type MDPTSProblems struct {
	set []*MDPTS
}

// Solve ...
func (p *MDPTSProblems) Solve() {
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

// MDPTS ...
type MDPTS struct {
	one    []int
	two    []int
	output int
}

// CreateMDPTS ...
func CreateMDPTS() s.Problem {
	set := make([]*MDPTS, 0, 4)

	set = append(set, &MDPTS{
		one:    []int{2, 1, -2, 5},
		two:    []int{3, 0, -6},
		output: 18,
	})

	set = append(set, &MDPTS{
		one:    []int{3, -2},
		two:    []int{2, -6, 7},
		output: 21,
	})

	set = append(set, &MDPTS{
		one:    []int{-1, -1},
		two:    []int{1, 1},
		output: -1,
	})

	return &MDPTSProblems{set}
}

func (p *MDPTS) solve() int {
	m, n := len(p.one), len(p.two)

	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}

	var val int

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			val = p.one[i] * p.two[j]
			dp[i][j] = val

			if i > 0 && dp[i-1][j] > dp[i][j] {
				dp[i][j] = dp[i-1][j]
			}

			if j > 0 && dp[i][j-1] > dp[i][j] {
				dp[i][j] = dp[i][j-1]
			}

			if i > 0 && j > 0 {
				// if excluding the (i, j) product pair
				if dp[i-1][j-1] > dp[i][j] {
					dp[i][j] = dp[i-1][j-1]
				}

				// if including the (i, j) product pair
				if dp[i-1][j-1]+val > dp[i][j] {
					dp[i][j] = dp[i-1][j-1] + val
				}
			}
		}
	}

	fmt.Println(dp)

	return dp[m-1][n-1]
}
