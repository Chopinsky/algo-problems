package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// NWPGProblems ...
type NWPGProblems struct {
	set []*NWPG
}

// Solve ...
func (p *NWPGProblems) Solve() {
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

// NWPG ...
type NWPG struct {
	data   int
	output int
}

// CreateNWPG ...
func CreateNWPG() s.Problem {
	set := make([]*NWPG, 0, 4)

	set = append(set, &NWPG{
		data:   1,
		output: 12,
	})

	set = append(set, &NWPG{
		data:   2,
		output: 54,
	})

	set = append(set, &NWPG{
		data:   3,
		output: 246,
	})

	set = append(set, &NWPG{
		data:   7,
		output: 106494,
	})

	set = append(set, &NWPG{
		data:   5000,
		output: 30228214,
	})

	return &NWPGProblems{set}
}

func (p *NWPG) solve() int {
	var mod uint64 = 1000000007

	last := p.data
	dp := make([][]uint64, last)
	dp[0] = []uint64{6, 6}

	for i := 1; i < last; i++ {
		a, b := 2*dp[i-1][0]+2*dp[i-1][1], 2*dp[i-1][0]+3*dp[i-1][1]
		dp[i] = []uint64{a % mod, b % mod}
	}

	return int((dp[last-1][0] + dp[last-1][1]) % mod)
}
