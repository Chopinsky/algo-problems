package problems

import (
	"fmt"

	d "../../Utils"
)

// LSRC ...
type LSRC struct {
	problems    []*LSRCProblem
	currProblem *LSRCProblem
}

// Build ...
func (p *LSRC) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *LSRC) Run() {
	var prb *LSRCProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcLSRC(), prb.output)
			} else {
				prb.calcLSRC()
			}
		}
	}
}

// ResetGlobals ...
func (p *LSRC) ResetGlobals() {
}

// LSRCProblem ...
type LSRCProblem struct {
	source string
	output int
}

// CreateLSRC ...
func CreateLSRC() *LSRC {
	problems := make([]*LSRCProblem, 0)

	problems = append(problems, &LSRCProblem{
		source: "abcabcbb",
		output: 3,
	})

	problems = append(problems, &LSRCProblem{
		source: "pwwkew",
		output: 3,
	})

	return &LSRC{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *LSRCProblem) calcLSRC() int {
	size, src := len(p.source), p.source

	if size <= 1 {
		return size
	}

	start, end := 0, 0
	longest := 1

	store := make(map[byte]int)
	store[src[0]] = 1

	for end < size-1 {
		end++
		store[src[end]]++

		for (store[src[start]] > 1 || store[src[end]] > 1) && start < end {
			store[src[start]]--
			start++
		}

		if end-start+1 > longest {
			if d.DEBUG {
				fmt.Println("new longest:", start, end, src[start:end+1])
			}

			longest = end - start + 1
		}
	}

	return longest
}
