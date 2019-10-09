package problems

import (
	"fmt"

	d "../../Utils"
)

// VP ...
type VP struct {
	source    int
	output    int
	testCount int
}

// CreateVP ...
func CreateVP() *VP {
	return &VP{}
}

// Build ...
func (p *VP) Build(test int) {
	p.ResetGlobals()
	p.testCount = 3

	switch test {
	case 1:
		p.source = 2
		p.output = 10

	case 2:
		p.source = 5
		p.output = 68

	default:
		p.source = 1
		p.output = 5

	}
}

// ResetGlobals ...
func (p *VP) ResetGlobals() {
}

// Run ...
func (p *VP) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcVP(p.source), p.output)
			} else {
				calcVP(p.source)
			}
		}
	}
}

func calcVP(count int) int {
	dp := make([]int, 5)
	for i := range dp {
		dp[i] = 1
	}

	var temp0, temp1, temp2, temp3, temp4 int = 1, 1, 1, 1, 1

	for i := 1; i < count; i++ {
		temp0 = dp[1]
		temp1 = dp[0] + dp[2]
		temp2 = dp[0] + dp[1] + dp[3] + dp[4]
		temp3 = dp[2] + dp[4]
		temp4 = dp[0]

		if i != count-1 {
			dp[0], dp[1], dp[2], dp[3], dp[4] = temp0, temp1, temp2, temp3, temp4
		}
	}

	return temp0 + temp1 + temp2 + temp3 + temp4
}
