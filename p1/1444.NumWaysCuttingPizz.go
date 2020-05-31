package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// NWCPProblems ...
type NWCPProblems struct {
	set []*NWCP
}

// Solve ...
func (p *NWCPProblems) Solve() {
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

// NWCP ...
type NWCP struct {
	data   []string
	k      int
	output int
}

// CreateNWCP ...
func CreateNWCP() s.Problem {
	set := make([]*NWCP, 0, 4)

	set = append(set, &NWCP{
		data:   []string{"A..", "AAA", "..."},
		k:      3,
		output: 3,
	})

	set = append(set, &NWCP{
		data:   []string{"A..", "AA.", "..."},
		k:      3,
		output: 1,
	})

	set = append(set, &NWCP{
		data:   []string{"A..", "A..", "..."},
		k:      1,
		output: 1,
	})

	return &NWCPProblems{set}
}

func (p *NWCP) solve() int {
	if p.k == 1 {
		return 1
	}

	data := p.data
	h, w := len(p.data), len(data[0])
	dp := make([][][]int, h)
	counter := make([][][]int, h)

	for i := 0; i < h; i++ {
		dp[i] = make([][]int, w)
		counter[i] = make([][]int, w)
	}

	for i := w - 1; i >= 0; i-- {
		for j := h - 1; j >= 0; j-- {
			if dp[j][i] == nil {
				dp[j][i] = make([]int, p.k)
				counter[j][i] = make([]int, 2)
			}

			hasApple := data[j][i] == byte('A')

			if hasApple {
				// cell with apple
				counter[j][i][0] = 1
				counter[j][i][1] = 1

				dp[j][i][0] = 1

				for k := 1; k < p.k; k++ {
					sum := 0

					if j < h-1 {
						sum += counter[j+1][i][0]*dp[j+1][i][k-1] + dp[j+1][i][k]
						sum %= mod
					}

					if i < w-1 {
						sum += counter[j][i+1][1]*dp[j][i+1][k-1] + dp[j][i+1][k]
						sum %= mod
					}

					dp[j][i][k] = sum
				}
			} else {
				// empty cell
				if j < h-1 && counter[j+1][i][0] > 0 {
					counter[j][i][0] = counter[j+1][i][0] + 1
				}

				if i < w-1 && counter[j][i+1][1] > 0 {
					counter[j][i][1] = counter[j][i+1][1] + 1
				}

				if (j < h-1 && dp[j+1][i][0] > 0) || (i < w-1 && dp[j][i+1][0] > 0) {
					dp[j][i][0] = 1
				}

				for k := 1; k < p.k; k++ {
					if j < h-1 {
						dp[j][i][k] += dp[j+1][i][k]
					}

					if i < w-1 {
						dp[j][i][k] += dp[j][i+1][k]
					}
				}
			}
		}
	}

	if s.DebugMode() {
		for i := 0; i < h; i++ {
			fmt.Println(dp[i])
		}

		for i := 0; i < h; i++ {
			fmt.Println(counter[i])
		}
	}

	return dp[0][0][p.k-1]
}

func (p *NWCP) solve1() int {
	if p.k == 1 {
		return 1
	}

	data := p.data
	h, w := len(p.data), len(data[0])

	dp := make([][][]int, h)
	rows := make([][]int, h)
	cols := make([][]int, w)

	for i := 0; i < h; i++ {
		dp[i] = make([][]int, w)
	}

	var rLen, cLen int

	for i := w - 1; i >= 0; i-- {
		if cols[i] == nil {
			cols[i] = make([]int, 0, h)
		}

		for j := h - 1; j >= 0; j-- {
			if rows[j] == nil {
				// fmt.Println("making rows for:", j, i, rows)
				rows[j] = make([]int, 0, w)
			}

			if i == w-1 && j == h-1 {
				dp[j][i] = make([]int, p.k)

				if data[j][i] == byte('A') {
					dp[j][i][0] = 1
				}

				continue
			}

			// fmt.Println("visiting:", j, i)

			hasApple := data[j][i] == byte('A')

			dp[j][i] = make([]int, p.k)
			if hasApple {
				dp[j][i][0] = 1
			}

			//TODO: this doesn't feel right, must use (val-j)*(dp[val][i][k-1] + dp[val][i][k]) instead

			if j < h-1 {
				// make a horizontal count, count from below
				cLen = len(cols[i])

				if !hasApple {
					for k := 0; k < p.k; k++ {
						dp[j][i][k] = dp[j+1][i][k]
					}

					if dp[j][i][0] > 0 {
						dp[j][i][0] = 1
					}
				} else if cLen > 0 {
					// k = 2: any cut between here and (before) the 1st 'A' in
					// the cols[i] is valid
					dp[j][i][1] = cols[i][0] - j

					// k > 2
					for idx := cLen - 1; idx >= 0; idx-- {
						val := cols[i][idx]

						for k := 2; k < p.k; k++ {
							if dp[val][i][k-1] == 0 {
								// no more matchings for this cell
								break
							}

							dp[j][i][k] += (val - j) * dp[val][i][k-1]
						}
					}
				} else {
					for k := 1; k < p.k; k++ {
						dp[j][i][k] = 1 * dp[j+1][i][k-1]
					}
				}
			}

			if i < w-1 {
				// make a vertical cut, count from right
				rLen = len(rows[j])

				if !hasApple {
					for k := 0; k < p.k; k++ {
						dp[j][i][k] += dp[j][i+1][k]
					}

					if dp[j][i][0] > 0 {
						dp[j][i][0] = 1
					}
				} else if rLen > 0 {
					// k = 2: any cut between here and (before) the 1st 'A' in
					// the cols[i] is valid
					dp[j][i][1] += rows[j][0] - i

					// k > 2
					for idx := rLen - 1; idx >= 0; idx-- {
						val := rows[j][idx]

						// if j == 1 && i == 0 {
						// 	fmt.Println("@(1, 0)", rLen, dp[j][i], val, dp[j][val])
						// }

						for k := 2; k <= p.k; k++ {
							if dp[j][val][k-1] == 0 {
								// no more matchings for this cell
								break
							}

							dp[j][i][k] += (val - i) * dp[j][val][k-1]
						}
					}
				} else {
					for k := 1; k < p.k; k++ {
						dp[j][i][k] += 1 * dp[j][i+1][k-1]
					}
				}
			}

			if hasApple {
				rows[j] = append(rows[j], i)
				cols[i] = append(cols[i], j)
			}
		}
	}

	for i := 0; i < h; i++ {
		fmt.Println(dp[i])
	}

	// fmt.Println("rows:", rows)
	// fmt.Println("cols:", cols)

	return dp[0][0][p.k-1]
}
