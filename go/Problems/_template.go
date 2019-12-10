package problems

import (
	"fmt"
)

// XXX ...
type XXX struct {
	problems []*XXXProblem
}

type XXXProblem struct {
	source []int
	output int
}

// CreateXXX ...
func CreateXXX() *XXX {
	problems := make([]*XXXProblem)

	problems = append(problems, &XXXProblem{
		src:    nil,
		output: -1,
	})

	return &XXX{
		problems,
	}
}

// Build ...
func (p *XXX) Build(test int) *XXXProblem {
	p.ResetGlobals()

	if test < len(p.problems) {
		return p.problems[test]
	}

	return p.problems[0]
}

// Run ...
func (p *XXX) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			problem := p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(problem.solveXXX(), p.output)
			} else {
				//calcXXX(problem)
			}
		}
	}
}

// ResetGlobals ...
func (p *XXX) ResetGlobals() {
}

func (p *XXXProblem) solveXXX() int {
	return -1
}
