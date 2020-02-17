package problems

import (
	"fmt"

	d "../../Utils"
)

// MCFB ...
type MCFB struct {
	problems    []*MCFBProblem
	currProblem *MCFBProblem
}

// Build ...
func (p *MCFB) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *MCFB) Run() {
	var prb *MCFBProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcMCFB(), prb.output)
			} else {
				prb.calcMCFB()
			}
		}
	}
}

// ResetGlobals ...
func (p *MCFB) ResetGlobals() {
}

// MCFBProblem ...
type MCFBProblem struct {
	status         []int
	candies        []int
	keys           [][]int
	containedBoxes [][]int
	initBoxes      []int
	output         int
}

// CreateMCFB ...
func CreateMCFB() *MCFB {
	problems := make([]*MCFBProblem, 0)

	problems = append(problems, &MCFBProblem{
		status:         []int{1, 0, 1, 0},
		candies:        []int{7, 5, 4, 100},
		keys:           [][]int{{}, {}, {1}, {}},
		containedBoxes: [][]int{{1, 2}, {3}, {}, {}},
		initBoxes:      []int{0},
		output:         16,
	})

	return &MCFB{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *MCFBProblem) calcMCFB() int {
	// p.buildCache()

	stack := append([]int(nil), p.initBoxes...)
	status := append([]int(nil), p.status...)
	total := 0

	var state int

	for len(stack) > 0 {
		idx := stack[0]
		state, stack = status[idx], stack[1:]

		if state == 0 {
			// locked, not visited
			status[idx] = -1
			continue
		}

		if state == 1 {
			// open, not visited yet
			total += p.candies[idx]
			status[idx] = 2

			for _, key := range p.keys[idx] {
				if d.DEBUG {
					fmt.Println("visiting box:" + string(key))
				}

				target := status[key]
				if target == 0 {
					// if it's locked and not visited, toggle it to the open state
					status[key] = 1
				} else if target == -1 {
					// if it's locked and visited, toggle it to the open state, and add to the queue
					status[key] = 1
					stack = append(stack, key)
				}
			}

			if len(p.containedBoxes[idx]) > 0 {
				// add all contained boxes into the queue to open
				stack = append(stack, p.containedBoxes[idx]...)
			}
		}
	}

	return total
}
