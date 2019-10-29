package problems

import (
	"fmt"

	d "../../Utils"
)

// DRS ...
type DRS struct {
	source    []int
	count     int
	output    int
	testCount int
}

// CreateDRS ...
func CreateDRS() *DRS {
	return &DRS{}
}

// Build ...
func (p *DRS) Build(test int) {
	p.ResetGlobals()
	p.testCount = 3

	switch test {
	case 1:
		p.source = []int{1, 1, 1, 1, 1, 1}
		p.count = 2
		p.output = 30

	case 2:
		p.source = []int{1, 1, 1, 2, 2, 3}
		p.count = 3
		p.output = 181

	default:
		p.source = []int{1, 1, 2, 2, 2, 3}
		p.count = 2
		p.output = 34

	}
}

// ResetGlobals ...
func (p *DRS) ResetGlobals() {
}

// Run ...
func (p *DRS) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcDRS(p.source, p.count), p.output)
			} else {
				calcDRS(p.source, p.count)
			}
		}
	}
}

func calcDRS(rollMax []int, count int) int {
	last, curr := make([][]int, 6), make([][]int, 6)
	for i, val := range rollMax {
		last[i] = make([]int, val)
		curr[i] = make([]int, val)
	}

	for i := 0; i < 6; i++ {
		last[i][0] = 1
	}

	if d.DEBUG {
		fmt.Println(last, curr)
	}

	for roll := 1; roll < count; roll++ {
		for i := 0; i < 6; i++ {
			// reset the current roll's state row, row[i][j] will be reset by the i==j logic
			// so we don't need to reset the val to 0 here, though row[i][0] needs to start
			// from 0, or we're stacking double the actual counts
			curr[i][0] = 0

			for j := 0; j < 6; j++ {
				if i == j {
					// speical count as we're running consecutive rolls
					for k := 1; k < rollMax[i]; k++ {
						curr[i][k] = last[i][k-1]
					}
				} else {
					// a roll with a different prior val
					for k := 0; k < len(last[j]); k++ {
						curr[i][0] += last[j][k]
					}
				}
			}
		}

		if roll != count-1 {
			moveVals(curr, last)
		}

		if d.DEBUG {
			fmt.Println("Roll: ", roll+1, "; States:", curr)
		}
	}

	total := 0
	for i := 0; i < 6; i++ {
		for j := 0; j < len(curr[i]); j++ {
			total += curr[i][j]
		}
	}

	return total
}

func moveVals(src, tgt [][]int) {
	for i := 0; i < len(src); i++ {
		for j := 0; j < len(src[i]); j++ {
			tgt[i][j] = src[i][j]
		}
	}
}
