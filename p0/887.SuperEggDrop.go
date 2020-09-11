package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// SEDProblems ...
type SEDProblems struct {
	set []*SED
}

// Solve ...
func (p *SEDProblems) Solve() {
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

// SED ...
type SED struct {
	data   int
	floors int
	output int
}

// CreateSED ...
func CreateSED() s.Problem {
	set := make([]*SED, 0, 4)

	set = append(set, &SED{
		data:   1,
		floors: 2,
		output: 2,
	})

	set = append(set, &SED{
		data:   2,
		floors: 6,
		output: 3,
	})

	set = append(set, &SED{
		data:   3,
		floors: 14,
		output: 4,
	})

	return &SEDProblems{set}
}

func (p *SED) solve() int {
	if p.data == 0 || p.floors == 0 {
		return 0
	}

	if p.data == 1 {
		return p.floors
	}

	dp := make([][]int, p.data+1)
	for i := range dp {
		dp[i] = make([]int, p.floors+1)

		if i == 0 {
			// no eggs, 0 move
			continue
		}

		for j := 1; j < p.floors+1; j++ {
			// if j == 0, no floors to try, moves == 0
			if i == 1 {
				// 1 egg, worst case scenario requires j moves (i.e. one move
				// for each floor)
				dp[i][j] = j
			} else {
				// set the state as `TBD`
				dp[i][j] = -1
			}
		}
	}

	return calcMoves(p.data, p.floors, dp)
}

func calcMoves(eggs, floors int, dp [][]int) int {
	// already calculated the situation, just return the result
	if dp[eggs][floors] != -1 {
		return dp[eggs][floors]
	}

	l, r := 1, floors

	for l <= r {
		// mid floors to try
		m := (l + r) / 2

		// if egg cracks dropped floor `m`
		lower := calcMoves(eggs-1, m-1, dp)

		// if egg does not crack dropped from floor `m`, we only care
		// the `m+1` to `floors` section, which has `floors-m` amount
		// of floors to try with
		upper := calcMoves(eggs, floors-m, dp)

		// moves to take to finish the test given (eggs, floors)
		moves := max(lower, upper) + 1

		// set with the optimal moves
		if dp[eggs][floors] == -1 || moves < dp[eggs][floors] {
			dp[eggs][floors] = moves
		}

		// now try to optimize the section taking the most steps to finish
		if lower > upper {
			r = m - 1
		} else {
			l = m + 1
		}
	}

	return dp[eggs][floors]
}
