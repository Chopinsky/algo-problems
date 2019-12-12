package problems

import (
	"fmt"

	d "../../Utils"
)

// SD ...
type SD struct {
	problems    []*SDProblem
	currProblem *SDProblem
}

// SDProblem ...
type SDProblem struct {
	source []int
	th     int
	output int
}

// CreateSD ...
func CreateSD() *SD {
	problems := make([]*SDProblem, 0)

	problems = append(problems, &SDProblem{
		source: []int{1, 2, 5, 9},
		th:     6,
		output: 5,
	})

	problems = append(problems, &SDProblem{
		source: []int{2, 3, 5, 7, 11},
		th:     11,
		output: 3,
	})

	problems = append(problems, &SDProblem{
		source: []int{19},
		th:     5,
		output: 4,
	})

	return &SD{
		problems:    problems,
		currProblem: nil,
	}
}

// Build ...
func (p *SD) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *SD) Run() {
	var prb *SDProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(prb.calcSD(), prb.output)
			} else {
				//calcSD(problem)
			}
		}
	}
}

// ResetGlobals ...
func (p *SD) ResetGlobals() {
}

func (p *SDProblem) calcSD() int {
	size := len(p.source)

	if size == 0 {
		return -1
	} else if size == 1 {
		return getDivider(p.source[0], p.th)
	}

	start, end := p.source[0], p.source[size-1]
	best := end

	for start < end {
		divisor := (start + end) / 2
		sum := 0

		for _, val := range p.source {
			sum += getDivider(val, divisor)

			if sum > p.th {
				break
			}
		}

		fmt.Println(start, end, divisor, sum)

		if sum > p.th {
			start = divisor + 1
		} else if sum < p.th {
			if divisor < best {
				best = divisor
			}

			end = divisor - 1
		} else {
			return divisor
		}
	}

	return best
}

func getDivider(src, tgt int) int {
	if src <= tgt {
		return 1
	}

	if src%tgt == 0 {
		return src / tgt
	}

	return (src / tgt) + 1
}
