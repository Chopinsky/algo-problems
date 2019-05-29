package problems

import (
	d "../Utils"
)

// TS ...
type TS struct {
	source []int
	sum    int
	output int
}

// CreateTS ...
func CreateTS() *TS {
	return &TS{}
}

// Build ...
func (p *TS) Build(test int) {
	switch test {
	case 1:
		p.source = []int{1, 2, 3, 4, 5}
		p.sum = 1
		p.output = 3

	default:
		p.source = []int{1, 1, 1, 1, 1}
		p.sum = 3
		p.output = 5

	}
}

// Run ...
func (p *TS) Run() {
	d.Output(p.calc(), p.output)
}

func (p *TS) calc() int {
	sum := 0
	size := len(p.source)

	for _, val := range p.source {
		sum += val
	}

	if sum < p.sum {
		// can't be done
		return -1
	}

	if sum == p.sum || sum == -p.sum {
		// sole possibility
		return 1
	}

	dp := make([]int, 2*sum+1)

	dp[p.source[0]+sum] = 1
	dp[-p.source[0]+sum] = 1

	var lastIdx, val int
	for j := 1; j < size; j++ {
		val = p.source[j]
		next := make([]int, 2*sum+1)

		for i := 0; i < 2*sum+1; i++ {
			// use "+" on j-th val
			if i >= val {
				lastIdx = i - val
				if dp[lastIdx] > 0 {
					next[i] += dp[lastIdx]
				}
			}

			// use "-" on j-th val
			if i <= 2*sum-val {
				lastIdx = i + val
				if dp[lastIdx] > 0 {
					next[i] += dp[lastIdx]
				}
			}
		}

		dp = next
	}

	d.Debug(dp, 0)

	result := dp[p.sum+sum]
	if result > 0 {
		// found result
		return result
	}

	// invalid result -- we can't get this val by any combo
	return -1
}
