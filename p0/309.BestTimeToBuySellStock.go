package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// BTTBSSProblems ...
type BTTBSSProblems struct {
	set []*BTTBSS
}

// Solve ...
func (p *BTTBSSProblems) Solve() {
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

// BTTBSS ...
type BTTBSS struct {
	data   []int
	output int
}

// CreateBTTBSS ...
func CreateBTTBSS() s.Problem {
	set := make([]*BTTBSS, 0, 4)

	set = append(set, &BTTBSS{
		data:   []int{1, 2, 3, 0, 2},
		output: 3,
	})

	return &BTTBSSProblems{set}
}

func (p *BTTBSS) solve() int {
	return maxProfit1(p.data)
}

func maxProfit1(prices []int) int {
	if prices == nil || len(prices) <= 1 {
		return 0
	}

	size := len(prices)

	if size == 2 {
		if prices[1] > prices[0] {
			return prices[1] - prices[0]
		}

		return 0
	}

	dp := make([][]int, size)
	for i := range dp {
		dp[i] = make([]int, 2)
	}

	dp[0][0] = -1 * prices[0] // buy/hold the stock
	dp[1][0] = 0              // sell the stock

	for i := 1; i < size; i++ {
		p := prices[i]

		dp[i][0] = dp[i-1][0]
		dp[i][1] = dp[i-1][1]

		if i >= 2 && dp[i-2][1]-p > dp[i][0] {
			dp[i][0] = dp[i-2][1] - p
		}

		if -1*p > dp[i][0] {
			dp[i][0] = -1 * p
		}

		if dp[i-1][0]+p > dp[i][1] {
			dp[i][1] = dp[i-1][0] + p
		}
	}

	fmt.Println(dp)

	if dp[size-1][0] > dp[size-1][1] {
		return dp[size-1][0]
	}

	return dp[size-1][1]
}
