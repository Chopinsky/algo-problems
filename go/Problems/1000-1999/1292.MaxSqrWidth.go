package problems

import (
	"fmt"

	d "../../Utils"
)

// MSW ...
type MSW struct {
	problems    []*MSWProblem
	currProblem *MSWProblem
}

// Build ...
func (p *MSW) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *MSW) Run() {
	var prb *MSWProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcMSW(), prb.output)
			} else {
				prb.calcMSW()
			}
		}
	}
}

// ResetGlobals ...
func (p *MSW) ResetGlobals() {
}

// MSWProblem ...
type MSWProblem struct {
	source    [][]int
	threshold int
	output    int
}

// CreateMSW ...
func CreateMSW() *MSW {
	problems := make([]*MSWProblem, 0)

	problems = append(problems, &MSWProblem{
		source: [][]int{
			{1, 1, 3, 2, 4, 3, 2},
			{1, 1, 3, 2, 4, 3, 2},
			{1, 1, 3, 2, 4, 3, 2},
		},
		output: 2,
	})

	problems = append(problems, &MSWProblem{
		source: [][]int{
			{1, 1, 3, 2, 4, 3, 2},
			{1, 1, 3, 2, 4, 3, 2},
			{1, 1, 3, 2, 4, 3, 2},
		},
		output: 2,
	})

	return &MSW{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *MSWProblem) calcMSW() int {
	return -1
}
