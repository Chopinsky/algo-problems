package problems

import (
	"fmt"

	d "../../Utils"
)

// LPI ...
type LPI struct {
	source    []int
	output    int
	testCount int
}

// CreateLPI ...
func CreateLPI() *LPI {
	return &LPI{}
}

// Build ...
func (p *LPI) Build(test int) {
	p.ResetGlobals()
	p.testCount = 3

	switch test {
	case 1:
		p.source = []int{9, 9, 6, 0, 6, 9, 6, 9, 9}
		p.output = 9

	case 2:
		p.source = []int{9, 6, 9, 0, 6, 9, 6, 9, 9}
		p.output = 9

	default:
		p.source = []int{9, 9, 6, 0, 6, 6, 9}
		p.output = 3

	}
}

// ResetGlobals ...
func (p *LPI) ResetGlobals() {
}

// Run ...
func (p *LPI) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcInterval2(p.source), p.output)
			} else {
				calcInterval2(p.source)
			}
		}
	}
}

func calcInterval(days []int) int {
	counts := make(map[int]int, len(days))
	curr, max := 0, 0

	for i := range days {
		if days[i] > 8 {
			curr++
			counts[curr] = i

			// first busy day, done
			if curr == 1 {
				max = 1
				continue
			}
		}

		// find the longest interval
		for j := 1; j < curr; j++ {
			// the tgt-th day that we had curr-j busy days
			tgt := counts[curr-j]

			d.Debug(fmt.Sprintln(i, curr, j, tgt, max), 0)

			// i-tgt+1 == total days in this interval
			// j+1     == total busy days
			// if `2*(j+1) <= i - tgt + 1`, then equal or less busy days than normal days in
			// this interval, no need to keep looking back, break; otherwise, update the `max`
			// value.
			if i-tgt < 2*j+1 {
				// a valid interval, extend to the maximum days
				currMax := d.Min(2*j+1, i+1)
				if currMax > max {
					max = currMax
				}
			} else {
				break
			}
		}
	}

	return max
}

func calcInterval2(days []int) int {
	sum, max := 0, 0
	index := make(map[int]int)

	for i := range days {
		if days[i] > 8 {
			sum++
		} else {
			sum--
		}

		if sum > 0 {
			// extra positive days, adding to the max interval
			max = i + 1
		} else {
			// only mark the 1st day we encounter the sum number, as this will yield the
			// longest interval
			if _, ok := index[sum]; !ok {
				index[sum] = i
			}

			// compare max with the day that has 1 less positive day, hence `i - j` will
			// yield +1 positive day
			if j, ok := index[sum-1]; ok {
				max = d.Max(max, i-j)
			}
		}
	}

	return max
}
