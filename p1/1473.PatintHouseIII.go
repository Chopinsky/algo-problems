package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// PHIIIProblems ...
type PHIIIProblems struct {
	set []*PHIII
}

// Solve ...
func (p *PHIIIProblems) Solve() {
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

// PHIII ...
type PHIII struct {
	data   []int
	cost   [][]int
	m      int
	n      int
	target int
	output int
}

// CreatePHIII ...
func CreatePHIII() s.Problem {
	set := make([]*PHIII, 0, 4)

	set = append(set, &PHIII{
		data:   []int{0, 0, 0, 0, 0},
		cost:   [][]int{{1, 10}, {10, 1}, {10, 1}, {1, 10}, {5, 1}},
		m:      5,
		n:      2,
		target: 3,
		output: 9,
	})

	set = append(set, &PHIII{
		data:   []int{0, 2, 1, 2, 0},
		cost:   [][]int{{1, 10}, {10, 1}, {10, 1}, {1, 10}, {5, 1}},
		m:      5,
		n:      2,
		target: 3,
		output: 11,
	})

	set = append(set, &PHIII{
		data:   []int{0, 0, 0, 0, 0},
		cost:   [][]int{{1, 10}, {10, 1}, {1, 10}, {10, 1}, {1, 10}},
		m:      5,
		n:      2,
		target: 5,
		output: 5,
	})

	set = append(set, &PHIII{
		data:   []int{3, 1, 2, 3},
		cost:   [][]int{{1, 1, 1}, {1, 1, 1}, {1, 1, 1}, {1, 1, 1}},
		m:      4,
		n:      3,
		target: 3,
		output: -1,
	})

	return &PHIIIProblems{set}
}

func (p *PHIII) solve() int {
	m, n, src, tgt, costs := p.m, p.n, p.data, p.target, p.cost
	dp := make([][][]int, m)

	for i := 0; i < m; i++ {
		dp[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]int, tgt)
			for k := 0; k < tgt; k++ {
				dp[i][j][k] = -1
			}
		}
	}

	// initialize
	color := src[0] - 1

	for i := 0; i < n; i++ {
		for j := 0; j < tgt; j++ {
			if color < 0 && j == 0 {
				dp[0][i][j] = costs[0][i] // cost
			} else if color == i && j == 0 {
				dp[0][i][j] = 0 // no cost
			}
		}
	}

	var val, cost int

	for i := 1; i < m; i++ { // i -- row
		color = src[i] - 1

		for j := 0; j < n; j++ { // j -- curr row's color
			if color >= 0 {
				// painted already
				if j == color {
					cost = 0 // no cost to paint
				} else {
					cost = -1 // illegal case
				}
			} else {
				cost = costs[i][j] // new paint cost
			}

			for k := 0; k < tgt; k++ { // k -- count
				for l := 0; l < n; l++ { // l -- last row's color
					if j == l && dp[i-1][j][k] >= 0 && cost >= 0 {
						// same color, then same n-count
						val = dp[i-1][j][k] + cost
					} else if k > 0 && dp[i-1][l][k-1] >= 0 && cost >= 0 {
						// different color, then n-count + 1 (i.e. looking at n-count - 1
						// from the last row)
						val = dp[i-1][l][k-1] + cost
					} else {
						// illegal cases
						val = -1
					}

					if val != -1 && (dp[i][j][k] == -1 || val < dp[i][j][k]) {
						dp[i][j][k] = val
					}
				}
			}
		}
	}

	best := -1
	for i := 0; i < n; i++ {
		val = dp[m-1][i][tgt-1]
		if best == -1 || (val != -1 && val < best) {
			best = val
		}
	}

	return best
}
