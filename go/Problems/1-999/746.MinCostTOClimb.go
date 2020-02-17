package problems

import (
	"fmt"

	d "../../Utils"
)

// MCC ...
type MCC struct {
	source    []int
	output    int
	testCount int
}

// CreateMCC ...
func CreateMCC() *MCC {
	return &MCC{}
}

// Build ...
func (p *MCC) Build(test int) {
	p.ResetGlobals()
	p.testCount = 2

	switch test {
	case 1:
		p.source = []int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}
		p.output = 6

	default:
		p.source = []int{10, 15, 20}
		p.output = 15

	}
}

// ResetGlobals ...
func (p *MCC) ResetGlobals() {
}

// Run ...
func (p *MCC) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(climb(p.source), p.output)
			} else {
				climb(p.source)
			}
		}

		fmt.Println()
	}
}

func climb(stairs []int) int {
	size := len(stairs)
	costs := make([]int, size+1)
	var one, two int

	for i := 2; i <= size; i++ {
		one = costs[i-1] + stairs[i-1]
		two = costs[i-2] + stairs[i-2]
		costs[i] = d.Min(one, two)
	}

	d.Debug(costs, 0)

	return costs[size]
}
