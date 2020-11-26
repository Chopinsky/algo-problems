package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MCTCTGPProblems ...
type MCTCTGPProblems struct {
	set []*MCTCTGP
}

// Solve ...
func (p *MCTCTGPProblems) Solve() {
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

// MCTCTGP ...
type MCTCTGP struct {
	data   [][]int
	output int
}

// CreateMCTCTGP ...
func CreateMCTCTGP() s.Problem {
	set := make([]*MCTCTGP, 0, 4)

	set = append(set, &MCTCTGP{
		data: [][]int{
			{15, 96}, {36, 2},
		},
		output: 17,
	})

	set = append(set, &MCTCTGP{
		data: [][]int{
			{1, 3, 5}, {4, 1, 1}, {1, 5, 3},
		},
		output: 4,
	})

	set = append(set, &MCTCTGP{
		data: [][]int{
			{2, 5, 1}, {3, 4, 7}, {8, 1, 2}, {6, 2, 4}, {3, 8, 8},
		},
		output: 10,
	})

	return &MCTCTGPProblems{set}
}

// MaxInt ...
const MaxInt = 1000000007

func (p *MCTCTGP) solve() int {
	cost := p.data
	h, w := len(p.data), len(p.data[0])
	statesCount := (1 << w) - 1 // from 0 to 1....1 with w 1s

	// dp[i][j] == min cost to connect first i points on the left, to the
	// points on the right and represented by state j
	dp := make([][]int, h+1)
	for i := range dp {
		dp[i] = make([]int, statesCount+1)
		for j := range dp[i] {
			if i == 0 && j == 0 {
				// init state: dp[0][0] = 0
				continue
			}

			dp[i][j] = MaxInt
		}
	}

	for i := 0; i < h; i++ {
		for s := 0; s <= statesCount; s++ {
			for j := 0; j < w; j++ {
				dp[i+1][s|(1<<j)] = min3(
					dp[i+1][s|(1<<j)],
					dp[i+1][s]+cost[i][j],
					dp[i][s]+cost[i][j],
				)
			}
		}
	}

	fmt.Println(dp)

	return dp[h][statesCount]
}

func min3(a, b, c int) int {
	if a <= b && a <= c {
		return a
	}

	if b <= a && b <= c {
		return b
	}

	return c
}
