package problems

import (
	"fmt"

	d "../../Utils"
)

// THD ...
type THD struct {
	source    []int
	output    int
	testCount int
}

// CreateTHD ...
func CreateTHD() *THD {
	return &THD{}
}

// Build ...
func (p *THD) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	switch test {
	default:
		p.source = []int{4, 14, 2}
		p.output = 6

	}
}

// ResetGlobals ...
func (p *THD) ResetGlobals() {
}

// Run ...
func (p *THD) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(sumHummingDist2(p.source), p.output)
			} else {
				sumHummingDist(p.source)
			}
		}
	}
}

func sumHummingDist(src []int) int {
	sum, size := 0, len(src)

	for i := 0; i < size-1; i++ {
		for j := i + 1; j < size; j++ {
			sum += calcHammingDist(src[i], src[j])
		}
	}

	return sum
}

func calcHammingDist(one, two int) int {
	count := 0

	base := one ^ two
	for base > 0 {
		count += base & 1
		base >>= 1
	}

	return count
}

func sumHummingDist2(src []int) int {
	m := make([][]int, 32)
	for i := range m {
		m[i] = make([]int, 2)
	}

	for i := range src {
		m = countDigits(src[i], m)
	}

	sum := 0
	for i := 0; i < 32; i++ {
		sum += m[i][0] * m[i][1]
	}

	return sum
}

func countDigits(num int, m [][]int) [][]int {
	count := 0
	for num > 0 {
		if num&1 == 1 {
			m[count][0]++
		} else {
			m[count][1]++
		}

		num >>= 1
		count++
	}

	return m
}
