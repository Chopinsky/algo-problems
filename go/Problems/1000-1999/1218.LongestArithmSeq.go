package problems

import (
	"fmt"

	d "../../Utils"
)

// LAS ...
type LAS struct {
	source    []int
	diff      int
	output    int
	testCount int
}

// CreateLAS ...
func CreateLAS() *LAS {
	return &LAS{}
}

// Build ...
func (p *LAS) Build(test int) {
	p.ResetGlobals()
	p.testCount = 3

	switch test {
	case 1:
		p.source = []int{1, 3, 5, 7}
		p.diff = 1
		p.output = 1

	case 2:
		p.source = []int{1, 5, 7, 8, 5, 3, 4, 2, 1}
		p.diff = -2
		p.output = 4

	default:
		p.source = []int{1, 2, 3, 4}
		p.diff = 1
		p.output = 4

	}
}

// ResetGlobals ...
func (p *LAS) ResetGlobals() {
}

// Run ...
func (p *LAS) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcLAS(p.source, p.diff), p.output)
			} else {
				calcLAS(p.source, p.diff)
			}
		}
	}
}

func calcLAS(src []int, diff int) int {
	result := 1
	store := make(map[int]int, len(src))

	for _, val := range src {
		tgt := val - diff

		if d.DEBUG {
			fmt.Println(val, tgt)
		}

		if last, ok := store[tgt]; ok {
			store[val] = last + 1
			if last+1 > result {
				result = last + 1
			}
		} else {
			store[val] = 1
		}
	}

	return result
}
