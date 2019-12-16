package problems

import (
	"fmt"
)

// XXX ...
type XXX struct {
	problems    []*XXXProblem
	currProblem *XXXProblem
}

// XXXProblem ...
type XXXProblem struct {
	source []int
	output int
}

// Build ...
func (p *XXX) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *XXX) Run() {
	var prb *XXXProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcXXX(), prb.output)
			} else {
				prb.calcXXX()
			}
		}
	}
}

// ResetGlobals ...
func (p *XXX) ResetGlobals() {
}

// CreateXXX ...
func CreateXXX() *XXX {
	problems := make([]*XXXProblem, 0)

	problems = append(problems, &XXXProblem{
		source: nil,
		output: -1,
	})

	return &XXX{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *XXXProblem) calcXXX() int {
	return -1
}
