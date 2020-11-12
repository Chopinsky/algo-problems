package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// PSProblems ...
type PSProblems struct {
	set []*PS
}

// Solve ...
func (p *PSProblems) Solve() {
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

// PS ...
type PS struct {
	data   []int
	profit []int
	P      int
	G      int
	output int
}

// CreatePS ...
func CreatePS() s.Problem {
	set := make([]*PS, 0, 4)

	set = append(set, &PS{
		data:   []int{2, 2},
		profit: []int{2, 3},
		P:      5,
		G:      3,
		output: 2,
	})

	set = append(set, &PS{
		data:   []int{2, 3, 5},
		profit: []int{6, 7, 8},
		P:      10,
		G:      5,
		output: 7,
	})

	set = append(set, &PS{
		data:   []int{2, 2},
		profit: []int{2, 3},
		P:      5,
		G:      3,
		output: 2,
	})

	set = append(set, &PS{
		data: []int{
			2, 5, 36, 2, 5, 5, 14, 1, 12, 1, 14, 15, 1, 1, 27, 13, 6, 59, 6, 1, 7, 1, 2, 7, 6, 1, 6, 1, 3, 1, 2, 11, 3, 39, 21, 20, 1, 27, 26, 22, 11, 17, 3, 2, 4, 5, 6, 18, 4, 14, 1, 1, 1, 3, 12, 9, 7, 3, 16, 5, 1, 19, 4, 8, 6, 3, 2, 7, 3, 5, 12, 6, 15, 2, 11, 12, 12, 21, 5, 1, 13, 2, 29, 38, 10, 17, 1, 14, 1, 62, 7, 1, 14, 6, 4, 16, 6, 4, 32, 48,
		},
		profit: []int{
			21, 4, 9, 12, 5, 8, 8, 5, 14, 18, 43, 24, 3, 0, 20, 9, 0, 24, 4, 0, 0, 7, 3, 13, 6, 5, 19, 6, 3, 14, 9, 5, 5, 6, 4, 7, 20, 2, 13, 0, 1, 19, 4, 0, 11, 9, 6, 15, 15, 7, 1, 25, 17, 4, 4, 3, 43, 46, 82, 15, 12, 4, 1, 8, 24, 3, 15, 3, 6, 3, 0, 8, 10, 8, 10, 1, 21, 13, 10, 28, 11, 27, 17, 1, 13, 10, 11, 4, 36, 26, 4, 2, 2, 2, 10, 0, 11, 5, 22, 6,
		},
		P:      100,
		G:      100,
		output: 692206787,
	})

	return &PSProblems{set}
}

func (p *PS) solve() int {
	return profitableSchemes(p.G, p.P, p.data, p.profit)
}

func profitableSchemes(G int, P int, group []int, profit []int) int {
	if len(group) == 0 || len(profit) == 0 {
		return 0
	}

	var dp map[int]map[int]int
	mod := 1000000007

	for i := range group {
		g := group[i]
		p := profit[i]

		if i > 0 {
			next := make(map[int]map[int]int)

			//todo
			for g0, p0 := range dp {
				if _, ok := next[g0]; !ok {
					next[g0] = make(map[int]int)
				}

				gg := g0 + g

				for pp, c := range p0 {
					// if don't do i-th crime
					next[g0][pp] = (next[g0][pp] + c) % mod

					// if can do i-th crime
					if gg <= G {
						if _, ok := next[gg]; !ok {
							next[gg] = make(map[int]int)
						}

						if pp+p >= P {
							next[gg][P] = (next[gg][P] + c) % mod
						} else {
							next[gg][pp+p] = (next[gg][pp+p] + c) % mod
						}
					}
				}
			}

			// if we only do this job
			if g <= G {
				if _, ok := next[g]; !ok {
					next[g] = make(map[int]int)
				}

				if p >= P {
					next[g][P]++
				} else {
					next[g][p]++
				}
			}

			dp = next
		} else {
			dp = make(map[int]map[int]int)
			if g > G {
				continue
			}

			dp[g] = make(map[int]int)
			if p >= P {
				dp[g][P] = 1
			} else {
				dp[g][p] = 1
			}
		}

		// fmt.Println(i, dp)
	}

	sum := 0

	for g, p := range dp {
		if g > G {
			continue
		}

		sum = (sum + p[P]) % mod
	}

	return sum % mod
}
