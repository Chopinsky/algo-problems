package problems

import (
	"fmt"
	"sort"

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

var numCount map[int]int

// ResetGlobals ...
func (p *DASKCN) ResetGlobals() {
	numCount = make(map[int]int)
}

// DASKCNProblem ...
type DASKCNProblem struct {
	source []int
	k      int
	output [][]int
}

// CreateDASKCN ...
func CreateDASKCN() *DASKCN {
	problems := make([]*DASKCNProblem, 0)

	problems = append(problems, &DASKCNProblem{
		source: []int{1, 2, 3, 3, 4, 4, 5, 6},
		k:      4,
		output: [][]int{{1, 2, 3, 4}, {3, 4, 5, 6}},
	})

	problems = append(problems, &DASKCNProblem{
		source: []int{3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11},
		k:      3,
		output: [][]int{{1, 2, 3}, {2, 3, 4}, {3, 4, 5}, {9, 10, 11}},
	})

	problems = append(problems, &DASKCNProblem{
		source: []int{3, 3, 2, 2, 1, 1},
		k:      3,
		output: [][]int{{1, 2, 3}, {1, 2, 3}},
	})

	problems = append(problems, &DASKCNProblem{
		source: []int{1, 2, 3, 4},
		k:      3,
		output: nil,
	})

	return &DASKCN{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *DASKCNProblem) buildCount() []int {
	numbers := make([]int, 0)

	for _, val := range p.source {
		if _, ok := numCount[val]; ok {
			numCount[val]++
		} else {
			numbers = append(numbers, val)
			numCount[val] = 1
		}
	}

	sort.Ints(numbers)

	return numbers
}

func (p *DASKCNProblem) calcDASKCN() bool {
	numbers := p.buildCount()

	var start int

	for len(numbers) > 0 {
		start, numbers = numbers[0], numbers[1:]
		if numCount[start] == 0 {
			continue
		}

		count := numCount[start]
		numCount[start] = 0

		for i := 1; i < p.k; i++ {
			if total, ok := numCount[start+i]; !ok || total < count {
				if d.DEBUG {
					fmt.Println(numCount)
					fmt.Println(start, start+i, count, ok)
				}

				return false
			}

			numCount[start+i] -= count
		}
	}

	return true
}
