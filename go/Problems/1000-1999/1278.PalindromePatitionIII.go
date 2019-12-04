package problems

import (
	"fmt"

	d "../../Utils"
)

// PPIII ...
type PPIII struct {
	source    string
	k         int
	output    int
	testCount int
}

// CreatePPIII ...
func CreatePPIII() *PPIII {
	return &PPIII{}
}

// Build ...
func (p *PPIII) Build(test int) {
	switch test {
	case 1:
		p.source = "aabbc"
		p.k = 3
		p.output = 0

	case 2:
		p.source = "leetcode"
		p.k = 8
		p.output = 0

	default:
		p.source = "abc"
		p.k = 2
		p.output = 1

	}

	p.ResetGlobals()
	p.testCount = 3
}

// Run ...
func (p *PPIII) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcPPIII(p.source, p.k), p.output)
			} else {
				//calcPPIII(p.source)
			}
		}
	}
}

// ResetGlobals ...
func (p *PPIII) ResetGlobals() {
	palindromCost = make(map[int]int)
}

var palindromCost map[int]int

func calcPPIII(src string, k int) int {
	preprocess(src)

	if d.DEBUG {
		for k, v := range palindromCost {
			fmt.Println(k, v)
		}
	}

	return runDpCalc(src, k)
}

func runDpCalc(src string, k int) int {
	dp := make([][]int, k)
	size := len(src)

	if k == size {
		return 0
	}

	for i := 0; i < k; i++ {
		dp[i] = make([]int, size+1)

		for j := i + 2; j <= size; j++ {
			if i == 0 {
				dp[i][j] = palindromCost[hashKey(i, j-1)]
			} else {
				dp[i][j] = 1 << 32
				for l := 1; l <= j-i+1; l++ {
					dp[i][j] = d.Min(dp[i][j], dp[i-1][j-l]+palindromCost[hashKey(j-l, j-1)])
				}
			}
		}
	}

	fmt.Println(dp)

	return dp[k-1][size]
}

func preprocess(src string) {
	size := len(src)
	for i := 0; i < size-1; i++ {
		count1, count2, offset := 0, 0, 1
		var start1, start2, end int

		for i-offset+1 >= 0 && i+offset < size {
			start1, start2, end = i-offset, i-offset+1, i+offset

			if start1 >= 0 {
				if src[start1] != src[end] {
					count1++
				}

				palindromCost[hashKey(start1, end)] = count1
			}

			if src[start2] != src[end] {
				count2++
			}

			palindromCost[hashKey(start2, end)] = count2

			offset++
		}
	}
}

func hashKey(i, j int) int {
	return i*100 + j
}
