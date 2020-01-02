package problems

import (
	"fmt"

	d "../../Utils"
)

// DASKCN ...
type DASKCN struct {
	problems    []*DASKCNProblem
	currProblem *DASKCNProblem
}

// Build ...
func (p *DASKCN) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *DASKCN) Run() {
	var prb *DASKCNProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcDASKCN(), prb.output)
			} else {
				prb.calcDASKCN()
			}
		}
	}
}

// ResetGlobals ...
func (p *DASKCN) ResetGlobals() {
}

// DASKCNProblem ...
type DASKCNProblem struct {
	source []int
	output int
}

// CreateDASKCN ...
func CreateDASKCN() *DASKCN {
	problems := make([]*DASKCNProblem, 0)

	problems = append(problems, &DASKCNProblem{
		source: nil,
		output: -1,
	})

	return &DASKCN{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *DASKCNProblem) calcDASKCN() int {
	return -1
}
