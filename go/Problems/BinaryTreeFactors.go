package problems

import (
	"fmt"

	d "../Debug"
)

// BTF ...
type BTF struct {
	source []int
	output int
}

// CreateBTF ...
func CreateBTF() *BTF {
	return &BTF{
		source: nil,
		output: 0,
	}
}

// Build ...
func (p *BTF) Build(test int) {
	switch test {
	case 1:
		p.source = []int{2, 4, 5, 10}
		p.output = 7

	default:
		p.source = []int{2, 4}
		p.output = 3

	}
}

// Run ...
func (p *BTF) Run() {
	dp := make(map[int]int)
	for _, val := range p.source {
		dp[val] = 1
	}

	for i := 1; i < len(p.source); i++ {
		for j := 0; j < i; j++ {
			root := p.source[i]
			left := p.source[j]

			if root%left == 0 {
				right := int(root / left)
				if val, ok := dp[right]; ok {
					dp[root] += dp[left] * val
				}
			}
		}
	}

	d.Debug(fmt.Sprintf("Resulting array: %v\n", dp), 0)

	sum := 0
	for _, val := range dp {
		sum += val
	}

	fmt.Println("Calculated result: ", sum)
	fmt.Println("Expected result: ", p.output)
}
