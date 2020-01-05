package problems

import (
	"fmt"

	d "../../Utils"
)

// ATN ...
type ATN struct {
	problems    []*ATNProblem
	currProblem *ATNProblem
}

// Build ...
func (p *ATN) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *ATN) Run() {
	var prb *ATNProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcATN(), prb.output)
			} else {
				prb.calcATN()
			}
		}
	}
}

// ResetGlobals ...
func (p *ATN) ResetGlobals() {
}

// ATNProblem ...
type ATNProblem struct {
	source [][]int
	output []int
}

// CreateATN ...
func CreateATN() *ATN {
	problems := make([]*ATNProblem, 0)

	problems = append(problems, &ATNProblem{
		source: [][]int{{2, 4, 3}, {5, 6, 4}},
		output: []int{7, 0, 8},
	})

	problems = append(problems, &ATNProblem{
		source: [][]int{{2, 4, 5}, {5, 6, 4}},
		output: []int{7, 0, 0, 1},
	})

	return &ATN{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *ATNProblem) calcATN() []int {
	remainder := 0
	result := make([]int, 0, len(p.source[0]))

	for i, val := range p.source[0] {
		sum := val + p.source[1][i] + remainder

		if sum >= 10 {
			sum -= 10
			remainder = 1
		} else {
			remainder = 0
		}

		result = append(result, sum)
	}

	if remainder == 1 {
		result = append(result, remainder)
	}

	return result
}
