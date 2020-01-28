package problems

import (
	"fmt"

	d "../../Utils"
)

// MDJS ...
type MDJS struct {
	problems    []*MDJSProblem
	currProblem *MDJSProblem
}

// Build ...
func (p *MDJS) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *MDJS) Run() {
	var prb *MDJSProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcMDJS(), prb.output)
			} else {
				// prb.calcMDJS()
			}
		}
	}
}

// ResetGlobals ...
func (p *MDJS) ResetGlobals() {
}

// MDJSProblem ...
type MDJSProblem struct {
	source []int
	day    int
	output int
}

// CreateMDJS ...
func CreateMDJS() *MDJS {
	problems := make([]*MDJSProblem, 0)

	problems = append(problems, &MDJSProblem{
		source: []int{6, 5, 4, 3, 2, 1},
		day:    2,
		output: 7,
	})

	problems = append(problems, &MDJSProblem{
		source: []int{9, 9, 9},
		day:    4,
		output: -1,
	})

	problems = append(problems, &MDJSProblem{
		source: []int{1, 1, 1},
		day:    3,
		output: 3,
	})

	problems = append(problems, &MDJSProblem{
		source: []int{7, 1, 7, 1, 7, 1},
		day:    3,
		output: 15,
	})

	problems = append(problems, &MDJSProblem{
		source: []int{11, 111, 22, 222, 33, 333, 44, 444},
		day:    6,
		output: 843,
	})

	return &MDJS{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *MDJSProblem) calcMDJS() int {
	size := len(p.source)
	if p.day > size {
		return -1
	}

	if p.day == size {
		sum := 0
		for i := 0; i < size; i++ {
			sum += p.source[i]
		}

		return sum
	}

	dp := make([][]int, size+1)
	for i := 0; i < size+1; i++ {
		dp[i] = make([]int, p.day+1)
		for j := 0; j < p.day+1; j++ {
			dp[i][j] = 1<<16 - 1
		}
	}

	dp[0][0] = 0

	for i := 1; i < size+1; i++ {
		for j := 1; j < p.day+1; j++ {
			md := 0
			for k := i - 1; k >= j-1; k-- {
				// update the top difficulty in the last day's job range
				if md < p.source[k] {
					md = p.source[k]
				}

				// the top difficulty in the last day's job range
				last := dp[k][j-1] + md

				if last < dp[i][j] {
					dp[i][j] = last
				}
			}
		}
	}

	return dp[size][p.day]
}
