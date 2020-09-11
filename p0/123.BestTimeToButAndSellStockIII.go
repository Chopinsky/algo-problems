package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// BTTBASSProblems ...
type BTTBASSProblems struct {
	set []*BTTBASS
}

// Solve ...
func (p *BTTBASSProblems) Solve() {
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

// BTTBASS ...
type BTTBASS struct {
	data   []int
	output int
}

// CreateBTTBASS ...
func CreateBTTBASS() s.Problem {
	set := make([]*BTTBASS, 0, 4)

	set = append(set, &BTTBASS{
		data:   []int{},
		output: 0,
	})

	return &BTTBASSProblems{set}
}

func (p *BTTBASS) solve() int {
	return 0
}

func maxProfit(prices []int) int {
	if prices == nil || len(prices) < 2 {
		return 0
	}

	size := len(prices)
	if size == 1 {
		return max(0, prices[1]-prices[0])
	}

	dp1 := make([][]int, size)
	dp2 := make([][]int, size)

	for i := range dp1 {
		dp1[i] = make([]int, 2)
		dp2[i] = make([]int, 2)

		if i == 0 {
			dp1[i][0] = prices[i]
		}

		if i == size-1 {
			dp2[i][0] = prices[i]
		}
	}

	for i := 1; i < size; i++ {
		dp1[i][0] = min(dp1[i-1][0], prices[i-1])
		dp1[i][1] = max(dp1[i-1][1], prices[i]-dp1[i][0])
	}

	for i := size - 2; i >= 0; i-- {
		dp2[i][0] = max(dp2[i+1][0], prices[i+1])
		dp2[i][1] = max(dp2[i+1][1], dp2[i][0]-prices[i])
	}

	best := max(dp1[size-1][1], dp2[0][1])
	for i := 1; i < size-2; i++ {
		val := dp1[i][1] + dp2[i+1][1]
		if val > best {
			best = val
		}
	}

	return best
}

func max(a, b int) int {
	if a <= b {
		return b
	}

	return a
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
