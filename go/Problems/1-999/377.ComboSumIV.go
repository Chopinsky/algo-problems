package problems

import (
	"fmt"
	"sort"

	d "../../Utils"
)

// CS4 ...
type CS4 struct {
	source    []int
	target    int
	output    int
	testCount int
}

// CreateCS4 ...
func CreateCS4() *CS4 {
	return &CS4{}
}

// Build ...
func (p *CS4) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	switch test {
	default:
		p.source = []int{1, 2, 3}
		p.target = 4
		p.output = 7

	}
}

// ResetGlobals ...
func (p *CS4) ResetGlobals() {
}

// Run ...
func (p *CS4) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calc(p.source, p.target), p.output)
			} else {
				calc(p.source, p.target)
			}
		}
	}
}

func calc(src []int, target int) int {
	dp := make([]int, target+1)

	sort.Ints(src)

	for i := 1; i < target+1; i++ {
		for j := range src {
			if src[j] > i {
				break
			}

			if src[j] == i {
				dp[i]++
			} else if dp[i-src[j]] > 0 {
				dp[i] += dp[i-src[j]]
			}
		}
	}

	d.Debug(dp, 0)

	return dp[target]
}
