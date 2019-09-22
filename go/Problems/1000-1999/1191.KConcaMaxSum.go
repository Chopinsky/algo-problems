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
	p.testCount = 6

	switch test {
	case 1:
		p.source = []int{1, -2, 1}
		p.k = 5
		p.output = 2

	case 2:
		p.source = []int{-1, -2}
		p.k = 7
		p.output = 0

	case 3:
		p.source = []int{-5, 2, -1, 3, -4}
		p.k = 4
		p.output = 4

	case 4:
		p.source = []int{2, -5, 1, 1}
		p.k = 11
		p.output = 4

	case 5:
		p.source = []int{-2, 5, 1, -3}
		p.k = 3
		p.output = 8

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
		fmt.Println("========= Running Trial: ", j, " =========")

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
		max, _, _ := calcSingleArr(src, 1)
		return max
	}

	// extend the src array to include the extension portion
	size := len(src)
	src = append(src, src...)

	// max1 is the global max, max2 is the original array max
	max1, max2, prefixSum := calcSingleArr(src, size)

	if d.DEBUG {
		fmt.Println(max1, max2, prefixSum[size])
	}

	// if adding more repetition will get us larger results
	if k > 2 && prefixSum[size] > 0 && max1 != max2 {
		max1 += (k - 2) * prefixSum[size]
	}

	if max1 > max2 {
		return max1
	}

	return max2
}

func calcSingleArr(src []int, originalSize int) (int, int, []int) {
	max1, max2, size := 0, 0, len(src)

	// extend the src array to include the extension portion
	prefixSum := make([]int, size+1)
	min := 0

	for i := range src {
		val := prefixSum[i] + src[i]

		if val < min {
			min = val
		} else {
			diff := val - min

			// the overall max
			if diff > max1 {
				max1 = diff
			}

			// the max from the sole array
			if i < originalSize && diff > max2 {
				max2 = diff
			}
		}

		prefixSum[i+1] = val
	}

	return max1, max2, prefixSum
}
