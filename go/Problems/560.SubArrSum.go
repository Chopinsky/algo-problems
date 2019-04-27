package problems

import (
	"fmt"

	d "../Utils"
)

var total []int
var totalMap map[int][]int

// SAS ...
type SAS struct {
	source []int
	sum    int
	output int
}

// CreateSAS ...
func CreateSAS() *SAS {
	return &SAS{}
}

// Build ...
func (p *SAS) Build(test int) {
	switch test {
	case 1:
		p.source = []int{1, 1, -1, 1}
		p.sum = 1
		p.output = 5

	default:
		p.source = []int{1, 1, 1}
		p.sum = 2
		p.output = 2

	}
}

// Run ...
func (p *SAS) Run() {
	size := len(p.source)
	factor := 1

	if p.sum < 0 {
		factor = -1
		p.sum *= factor
	}

	total = make([]int, size)
	total[0] = factor * p.source[0]

	totalMap = make(map[int][]int)
	totalMap[total[0]] = []int{0}

	for i := 1; i < size; i++ {
		total[i] = total[i-1] + factor*p.source[i]
		totalMap[total[i]] = append(totalMap[total[i]], i)
	}

	d.Debug(totalMap, 0)

	//count := p.calc()
	count := p.calcAlt()

	fmt.Println("Calculated result: ", count)
	fmt.Println("Expected result: ", p.output)
}

func (p *SAS) calcAllPositive() int {
	var fast, slow, count, s int

	for {
		// calc the subarray sum
		s = getSum(slow, fast)
		if s == p.sum {
			count++
		}

		// moving the pointers
		if s <= p.sum {
			fast++

			if fast >= size {
				break
			}
		} else {
			slow++

			if slow >= size {
				break
			}

			// don't fall behind
			if fast < slow {
				fast = slow
			}
		}
	}

	return count
}

func (p *SAS) calc() int {
	var count int

	size := len(p.source)
	for i := 0; i < size; i++ {
		for j := i; j < size; j++ {
			if total[j] < total[i] {
				continue
			}

			if getSum(i, j) == p.sum {
				count++
			}
		}
	}

	return count
}

func (p *SAS) calcAlt() int {
	var count int
	size := len(p.source)

	for i := 0; i < size; i++ {
		val := total[i] - p.sum

		// a match: [0, i]
		if val == 0 {
			count++
		}

		if arr, ok := totalMap[val]; ok {
			for _, cand := range arr {
				if cand <= i {
					count++
				}
			}
		}
	}

	return count
}

func getSum(i, j int) int {
	if i == 0 {
		return total[j]
	}

	return total[j] - total[i-1]
}
