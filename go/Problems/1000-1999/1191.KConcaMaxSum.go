package problems

import (
	"fmt"

	d "../../Utils"
)

// KCMS ...
type KCMS struct {
	source    []int
	k         int
	output    int
	testCount int
}

// CreateKCMS ...
func CreateKCMS() *KCMS {
	return &KCMS{}
}

// Build ...
func (p *KCMS) Build(test int) {
	p.ResetGlobals()
	p.testCount = 3

	switch test {
	case 1:
		p.source = []int{1, -2, 1}
		p.k = 5
		p.output = 2

	case 2:
		p.source = []int{-1, -2}
		p.k = 7
		p.output = 0

	default:
		p.source = []int{1, 2}
		p.k = 3
		p.output = 9

	}
}

// ResetGlobals ...
func (p *KCMS) ResetGlobals() {
}

// Run ...
func (p *KCMS) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcKCMS(p.source, p.k), p.output)
			} else {
				calcKCMS(p.source, p.k)
			}
		}
	}
}

func calcKCMS(src []int, k int) int {
	if k == 1 {
		result, _ := calcSoleArr(src)
		return result
	}

	// extend the src array to include the extension portion
	size := len(src)
	src = append(src, src...)
	result, prefixSum := calcSoleArr(src)

	if d.DEBUG {
		fmt.Println(result, prefixSum)
	}

	// if adding more repetition will get us larger results
	if k > 2 && prefixSum[size] > 0 {
		result += (k - 2) * prefixSum[size]
	}

	return result
}

func calcSoleArr(src []int) (int, []int) {
	result, size := 0, len(src)

	// extend the src array to include the extension portion
	prefixSum := make([]int, size+1)
	min := 0

	for i := range src {
		val := prefixSum[i] + src[i]

		if val < min {
			min = val
		} else if val-min > result {
			result = val - min
		}

		prefixSum[i+1] = val
	}

	return result, prefixSum
}
