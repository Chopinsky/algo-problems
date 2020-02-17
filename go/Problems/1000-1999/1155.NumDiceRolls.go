package problems

import (
	"fmt"

	di "../../Utils"
)

// NDR ...
type NDR struct {
	d         int
	f         int
	target    int
	output    int
	testCount int
}

// CreateNDR ...
func CreateNDR() *NDR {
	return &NDR{}
}

// Build ...
func (p *NDR) Build(test int) {
	p.ResetGlobals()
	p.testCount = 5

	switch test {
	case 1:
		p.d = 2
		p.f = 6
		p.target = 7
		p.output = 6

	case 2:
		p.d = 30
		p.f = 30
		p.target = 500
		p.output = 222616187

	case 3:
		p.d = 2
		p.f = 5
		p.target = 10
		p.output = 1

	case 4:
		p.d = 1
		p.f = 2
		p.target = 3
		p.output = 0

	default:
		p.d = 1
		p.f = 6
		p.target = 3
		p.output = 1

	}
}

// ResetGlobals ...
func (p *NDR) ResetGlobals() {
}

// Run ...
func (p *NDR) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				di.Output(calcNDR(p.d, p.f, p.target), p.output)
			} else {
				calcNDR(p.d, p.f, p.target)
			}
		}
	}
}

func calcNDR(d, f, target int) uint64 {
	if target > d*f {
		return 0
	}

	di.Debug(fmt.Sprintln(d, f, target), 0)

	mask := uint64(1000000007)
	dp := make([]uint64, f+1)

	for i := 1; i <= f; i++ {
		dp[i] = 1
	}

	// iterate over dices
	for i := 2; i <= d; i++ {
		next := make([]uint64, di.Min(i*f, target)+1)
		last := (i - 1) * f

		// iterate over all possible values
		for j := i; j <= di.Min(i*f, target); j++ {
			sum := uint64(0)

			// iterate over the combo of the new dice + existing combos
			for k := di.Max(1, j-last); k <= di.Min(j, f); k++ {
				sum += dp[j-k]
				sum %= mask
			}

			next[j] = sum
		}

		dp = next
	}

	di.Debug(fmt.Sprintln(dp), 0)

	return dp[target] % mask
}
