package problems

import (
	"fmt"

	d "../../Utils"
)

// PW ...
type PW struct {
	source []int
	win    bool
}

// CreatePW ...
func CreatePW() *PW {
	return &PW{
		source: nil,
		win:    false,
	}
}

// Build ...
func (p *PW) Build(test int) {
	switch test {
	case 1:
		p.source = []int{1, 5, 233, 7}
		p.win = true

	default:
		p.source = []int{1, 5, 2}
		p.win = false

	}
}

// Run ...
func (p *PW) Run() {
	fmt.Println("Exptected result: ", p.win)
	fmt.Println("Calculated result: ", p.simulate())
}

func (p *PW) simulate() bool {
	size := len(p.source)
	if size <= 2 {
		return true
	}

	// initialize the dp array
	dp := make([][][]int, size)
	for i := range dp {
		dp[i] = make([][]int, size)
		for j := range dp[i] {
			dp[i][j] = make([]int, 2)
		}
	}

	// initialize the source vals
	for i := 0; i < size; i++ {
		dp[i][i][0] = p.source[i]
		if i < size-1 {
			if p.source[i] > p.source[i+1] {
				dp[i][i+1][0] = p.source[i]
				dp[i][i+1][1] = p.source[i+1]
			} else {
				dp[i][i+1][0] = p.source[i+1]
				dp[i][i+1][1] = p.source[i]
			}
		}
	}

	// calculate
	for step := 2; step < size; step++ {
		for i := 0; i < size-step; i++ {
			j := i + step
			if (p.source[j] + dp[i][j-1][1]) > (p.source[i] + dp[i+1][j][1]) {
				dp[i][j][0] = p.source[j] + dp[i][j-1][1]
				dp[i][j][1] = dp[i][j-1][0]
			} else {
				dp[i][j][0] = p.source[i] + dp[i+1][j][1]
				dp[i][j][1] = dp[i+1][j][0]
			}
		}
	}

	d.Debug(dp, 0)

	return dp[0][size-1][0] >= dp[0][size-1][1]
}
