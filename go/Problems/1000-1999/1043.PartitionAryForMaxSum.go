package problems

import (
	"fmt"
	"strconv"

	d "../../Utils"
)

var subaryMax = make(map[string]int)

// PAMS ...
type PAMS struct {
	source []int
	length int
	output int
}

// CreatePAMS ...
func CreatePAMS() *PAMS {
	return &PAMS{}
}

// Build ...
func (p *PAMS) Build(test int) {
	switch test {
	default:
		p.source = []int{1, 15, 7, 9, 2, 5, 10}
		p.length = 3
		p.output = 84

	}
}

// Run ...
func (p *PAMS) Run() {
	fmt.Println("Calculated result: ", p.eval())
	fmt.Println("Expected result: ", p.output)
}

func (p *PAMS) eval() int {
	dp := make([][]int, p.length)
	size := len(p.source)

	for i := range dp {
		dp[i] = make([]int, size)
		dp[i][0] = p.source[0]

		for j := 1; j < size; j++ {
			if i > 0 {
				max := 0

				// vertical maximum check: the largest sum with less subarray length, total legit
				for ii := 0; ii < i; ii++ {
					if dp[ii][j] > max {
						max = dp[ii][j]
					}
				}

				// horizontal maximum check: the largest sum with less element plus new ones as the
				// extra subarray
				val := 0
				subMax := p.source[j]

				for jj := 1; jj <= d.Min(j, p.length); jj++ {
					//val = dp[i][j-jj] + p.findMax(j-jj+1, j)*jj
					subMax = d.Max(subMax, p.source[j-jj+1])
					val = dp[i][j-jj] + subMax*jj

					if val > max {
						max = val
					}
				}

				// horizontal case, if the whole array can be the sole subarray
				if j < p.length {
					//val = p.findMax(0, j) * (j + 1)
					val = d.Max(subMax, p.source[0]) * (j + 1)

					if val > max {
						max = val
					}
				}

				dp[i][j] = max
			} else {
				dp[0][j] = dp[0][j-1] + p.source[j]
			}
		}
	}

	d.Debug(dp, 0)

	return dp[p.length-1][size-1]
}

func (p *PAMS) findMax(low, high int) int {
	if low > high {
		return 0
	}

	if low == high {
		return p.source[high]
	}

	key := strconv.Itoa(low) + "," + strconv.Itoa(high)
	if val, ok := subaryMax[key]; ok {
		return val
	}

	max := 0
	for i := low; i <= high; i++ {
		if p.source[i] > max {
			max = p.source[i]
		}
	}

	subaryMax[key] = max
	return max
}
