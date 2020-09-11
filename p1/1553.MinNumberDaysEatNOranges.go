package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MNDENOProblems ...
type MNDENOProblems struct {
	set []*MNDENO
}

// Solve ...
func (p *MNDENOProblems) Solve() {
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

// MNDENO ...
type MNDENO struct {
	data   int
	output int
}

// CreateMNDENO ...
func CreateMNDENO() s.Problem {
	set := make([]*MNDENO, 0, 4)

	set = append(set, &MNDENO{
		data:   10,
		output: 4,
	})

	set = append(set, &MNDENO{
		data:   6,
		output: 3,
	})

	set = append(set, &MNDENO{
		data:   1,
		output: 1,
	})

	set = append(set, &MNDENO{
		data:   56,
		output: 6,
	})

	set = append(set, &MNDENO{
		data:   1999999997,
		output: 36,
	})

	return &MNDENOProblems{set}
}

func (p *MNDENO) solve1() int {
	if p.data <= 3 {
		return 1
	}

	dp := make(map[int]int)
	dp[p.data] = 0

	stack := []int{}
	stack = append(stack, p.data)

	var curr, rem, days, best int
	best = p.data

	for len(stack) > 0 {
		curr, stack = stack[0], stack[1:]
		days = dp[curr]

		if days >= best {
			continue
		}

		if curr%2 == 0 {
			rem = curr - (curr / 2)
			if d, ok := dp[rem]; !ok || (ok && days+1 < d) {
				dp[rem] = days + 1

				if rem != 0 {
					stack = append(stack, rem)
				}
			}

			if rem == 0 && days+1 < best {
				best = days + 1
			}
		}

		if curr%3 == 0 {
			rem = curr - 2*(curr/3)
			if d, ok := dp[rem]; !ok || (ok && days+1 < d) {
				dp[rem] = days + 1

				if rem != 0 {
					stack = append(stack, rem)
				}
			}

			if rem == 0 && days+1 < best {
				best = days + 1
			}
		}

		rem = curr - 1
		if d, ok := dp[rem]; !ok || (ok && days+1 < d) {
			dp[rem] = days + 1

			if rem != 0 {
				stack = append(stack, rem)
			}
		}

		if rem == 0 && days+1 < best {
			best = days + 1
		}
	}

	// fmt.Println(dp)

	return best
}

func (p *MNDENO) solve() int {
	return dp(p.data, make(map[int]int))
}

func dp(n int, cache map[int]int) int {
	if n <= 1 {
		return n
	}

	if val, ok := cache[n]; ok {
		return val
	}

	a := n%2 + dp(n/2, cache)
	b := n%3 + dp(n/3, cache)

	ans := 1
	if a < b {
		ans += a
	} else {
		ans += b
	}

	cache[n] = ans
	return ans
}
