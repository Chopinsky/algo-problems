package problems

import (
	"fmt"

	d "../Utils"
)

// SCSS ...
type SCSS struct {
	src1   string
	src2   string
	output string
}

// CreateSCSS ...
func CreateSCSS() *SCSS {
	return &SCSS{}
}

// Build ...
func (p *SCSS) Build(test int) {
	switch test {
	case 1:
		p.src1 = "abac"
		p.src2 = "cacbc"
		p.output = "cacbac"

	default:
		p.src1 = "abac"
		p.src2 = "cab"
		p.output = "cabac"

	}
}

// Run ...
func (p *SCSS) Run() {
	d.Output(p.find(), p.output)
}

func (p SCSS) find() string {
	size1, size2 := len(p.src1), len(p.src2)
	dp := lcsTab(p.src1, p.src2, size1, size2)

	i, j := size1, size2
	result := ""
	var char1, char2 string

	// follow in backwards on the trace where we obtained the lcs
	for i > 0 || j > 0 {
		if i == 0 && j > 0 {
			j--
			result = getChar(p.src2, j) + result
			continue
		}

		if j == 0 && i > 0 {
			i--
			result = getChar(p.src1, i) + result
			continue
		}

		char1, char2 = getChar(p.src1, i-1), getChar(p.src2, j-1)
		if char1 == char2 {
			result = char1 + result
			i--
			j--
			continue
		}

		if dp[i-1][j] == dp[i][j] {
			i--
			result = char1 + result
			continue
		}

		if dp[i][j-1] == dp[i][j] {
			j--
			result = char2 + result
			continue
		}
	}

	return result
}

// least common sequence ...
func lcsTab(src1, src2 string, size1, size2 int) [][]int {
	dp := make([][]int, size1+1)
	for i := range dp {
		dp[i] = make([]int, size2+1)
	}

	for i := 1; i <= size1; i++ {
		for j := 1; j <= size2; j++ {
			if src1[i-1] == src2[j-1] {
				dp[i][j] = 1 + dp[i-1][j-1]
			} else {
				dp[i][j] = d.Max(dp[i-1][j], dp[i][j-1])
			}
		}
	}

	if d.DEBUG {
		for _, val := range dp {
			fmt.Println(val)
		}
	}

	return dp
}

func getChar(s string, i int) string {
	return string(s[i])
}
