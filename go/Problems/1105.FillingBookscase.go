package problems

import (
	"fmt"

	d "../Utils"
)

// FBS ...
type FBS struct {
	// p.source[i][0] == book thickness;
	// p.source[i][1] == book height;
	source     [][]int
	totalWidth int
	output     int
	testCount  int
}

// CreateFBS ...
func CreateFBS() *FBS {
	return &FBS{}
}

// Build ...
func (p *FBS) Build(test int) {
	p.ResetGlobals()
	p.testCount = 3

	switch test {
	case 1:
		p.source = [][]int{
			{2, 1},
			{3, 4},
			{5, 7},
			{3, 1},
			{1, 6},
		}
		p.totalWidth = 20
		p.output = 7

	case 2:
		p.source = [][]int{
			{1, 1},
			{2, 3},
			{2, 3},
			{1, 1},
			{1, 1},
			{1, 1},
			{1, 2},
		}
		p.totalWidth = 4
		p.output = 6

	default:
		p.source = [][]int{
			{2, 1},
			{3, 4},
			{5, 7},
			{3, 1},
			{1, 6},
		}
		p.totalWidth = 5
		p.output = 17

	}
}

// ResetGlobals ...
func (p *FBS) ResetGlobals() {
}

// Run ...
func (p *FBS) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			fmt.Println("\nTest case: ", i, ":")
			d.Output(p.calc(), p.output)
		}

		fmt.Println()
	}
}

func buildDP(num int) [][]int {
	dp := make([][]int, num)
	for i := range dp {
		dp[i] = make([]int, 3)
	}

	return dp
}

func (p *FBS) calc() int {
	n := len(p.source)
	dp := buildDP(n)

	dp[0][0] = p.totalWidth - p.source[0][0] // remainder width on the last shelf
	dp[0][1] = p.source[0][1]                // shelf height
	dp[0][2] = p.source[0][1]                // max height on the last shelf

	var width, height, nextHeight int
	for i := 1; i < n; i++ {
		width, height = p.source[i][0], p.source[i][1]
		if width <= dp[i-1][0] {
			// if the book can be placed in the last shelf, i.e. no new shelf
			dp[i][0] = dp[i-1][0] - width
			dp[i][2] = d.Max(dp[i-1][2], height)

			if height > dp[i-1][2] {
				dp[i][1] = dp[i-1][1] + height - dp[i-1][2]
			} else {
				dp[i][1] = dp[i-1][1]
			}

			continue
		}

		// if book in a new shelf
		remainder, minHeight, shelfHeight := p.totalWidth-width, height+dp[i-1][1], height

		for j := i - 1; j >= 0; j-- {
			if width >= p.totalWidth {
				// no more book to be added into this shelf
				break
			}

			// add book j-th to this shelf, plus the min height with j-1 books
			width = width + p.source[j][0]
			if width > p.totalWidth {
				// not a valid combo, break
				break
			}

			height = d.Max(height, p.source[j][1])
			if j > 0 {
				// add
				nextHeight = height + dp[j-1][1]
			} else {
				// all books up to j can be placed in one shelf
				nextHeight = height
			}

			if nextHeight < minHeight {
				remainder, minHeight, shelfHeight = p.totalWidth-width, nextHeight, height
			}
		}

		dp[i][0], dp[i][1], dp[i][2] = remainder, minHeight, shelfHeight
	}

	for i := range dp {
		fmt.Println(dp[i])
	}

	return dp[n-1][1]
}
