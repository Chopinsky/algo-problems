package problems

import (
	"math"

	d "../../Utils"
)

// RAN ...
type RAN struct {
	source int
	output int
}

// CreateRAN ...
func CreateRAN() *RAN {
	return &RAN{}
}

// Build ...
func (p *RAN) Build(test int) {
	switch test {
	case 1:
		p.source = 15
		p.output = 5

	case 2:
		p.source = 64
		p.output = 11

	case 3:
		p.source = 2
		p.output = 3

	default:
		p.source = 3
		p.output = 2

	}
}

// Run ...
func (p *RAN) Run() {
	d.Output(walk(p.source), p.output)
}

func walk(target int) int {
	var step, max int
	isOdd := (target%2 == 1)
	step = int((math.Sqrt(float64(8*target+1)) / 2.0))

	for {
		max = step * (step + 1) / 2
		if max == target {
			break
		}

		if max > target && (max%2 == 1) == isOdd {
			break
		}

		step++
	}

	return step
}
