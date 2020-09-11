package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// NSOSProblems ...
type NSOSProblems struct {
	set []*NSOS
}

// Solve ...
func (p *NSOSProblems) Solve() {
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

// NSOS ...
type NSOS struct {
	data   []int
	output int
}

// CreateNSOS ...
func CreateNSOS() s.Problem {
	set := make([]*NSOS, 0, 4)

	set = append(set, &NSOS{
		data:   []int{1, 3, 5},
		output: 4,
	})

	set = append(set, &NSOS{
		data:   []int{2, 4, 6},
		output: 0,
	})

	set = append(set, &NSOS{
		data:   []int{1, 2, 3, 4, 5, 6, 7},
		output: 16,
	})

	set = append(set, &NSOS{
		data:   []int{100, 100, 99, 99},
		output: 4,
	})

	set = append(set, &NSOS{
		data:   []int{7},
		output: 1,
	})

	return &NSOSProblems{set}
}

func (p *NSOS) solve() int {
	// if number is odd, curr count is curr odd = prev even + 1 (self),
	// curr even = prev odd; if number is event, curr count is curr odd
	// = prev odd, curr even = prev even + 1 (self).

	var ans, odd, even int

	for _, v := range p.data {
		if v&1 == 1 {
			// if odd
			odd, even = even+1, odd
		} else {
			even = even + 1
		}

		ans = (ans + odd) % mod
	}

	return ans
}

func (p *NSOS) solve1() int {
	odds := make([]int, 0, len(p.data))
	size := len(p.data)

	for i, v := range p.data {
		if v%2 == 1 {
			odds = append(odds, i)
		}
	}

	sum := 0
	last := len(odds) - 1
	dp := make([]int, last+1)

	var before, after int

	// fmt.Println("src:", p.data)

	for i, pos := range odds {
		if i == 0 {
			before = pos + 1
		} else {
			before = pos - odds[i-1]

			if i > 1 {
				before += dp[i-2]
			}
		}

		if i == last {
			after = size - pos
		} else {
			after = odds[i+1] - pos
		}

		// fmt.Println(pos, before, after)

		dp[i] = before
		sum += ((before * after) % mod) % mod
	}

	// fmt.Println("dp:", dp)

	return sum
}
