package problems

import (
	"fmt"

	d "../../Utils"
)

var sum []int
var dp [][][]float32

// LSA ...
type LSA struct {
	source []int
	k      int
	output int
}

// CreateLSA ...
func CreateLSA() *LSA {
	return &LSA{}
}

// Build ...
func (p *LSA) Build(test int) {
	switch test {
	default:
		p.source = []int{9, 1, 2, 3, 9}
		p.k = 3
		p.output = 20

	}
}

// Run ...
func (p *LSA) Run() {
	size := p.init()
	fmt.Println("Calculated result: ", p.calc(0, size-1, p.k))
	fmt.Println("Expected result: ", p.output)
}

func (p *LSA) init() int {
	size := len(p.source)

	sum = make([]int, size)
	sum[0] = p.source[0]

	for i := 1; i < size; i++ {
		sum[i] = sum[i-1] + p.source[i]
	}

	dp = make([][][]float32, size)
	for i := range dp {
		dp[i] = make([][]float32, size)
		for j := range dp[i] {
			dp[i][j] = make([]float32, p.k+1)
		}
	}

	return size
}

func (p *LSA) calc(i, j, k int) float32 {
	if dp[i][j][k] > 0 || k == 0 {
		return dp[i][j][k]
	}

	if k == 1 {
		if dp[i][j][1] == 0 {
			dp[i][j][1] = getSumAverage(i, j)
		}

		return dp[i][j][1]
	}

	var max, res float32
	for m := i; m <= j-k+1; m++ {
		if dp[i][m][1] == 0 {
			dp[i][m][1] = getSumAverage(i, m)
		}

		if dp[m+1][j][k-1] == 0 {
			dp[m+1][j][k-1] = p.calc(m+1, j, k-1)
		}

		res = dp[i][m][1] + dp[m+1][j][k-1]
		if res > max {
			if i == 0 && j == len(p.source)-1 {
				d.Debug(fmt.Sprintln(m, ":", dp[i][m][1], dp[m+1][j][k-1]), 0)
			}

			max = res
		}
	}

	dp[i][j][k] = max
	return max
}

func getSumAverage(i, j int) float32 {
	if i == 0 {
		return float32(sum[j]) / float32(j+1)
	}

	return float32(sum[j]-sum[i-1]) / float32(j-i+1)
}
