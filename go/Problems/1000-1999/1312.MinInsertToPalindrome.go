package problems

import (
	"fmt"
	"math"

	d "../../Utils"
)

// MISP ...
type MISP struct {
	problems    []*MISPProblem
	currProblem *MISPProblem
}

// Build ...
func (p *MISP) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *MISP) Run() {
	var prb *MISPProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcMISP(), prb.output)
			} else {
				prb.calcMISP()
			}
		}
	}
}

// ResetGlobals ...
func (p *MISP) ResetGlobals() {
}

// MISPProblem ...
type MISPProblem struct {
	source string
	output int
}

// CreateMISP ...
func CreateMISP() *MISP {
	problems := make([]*MISPProblem, 0)

	problems = append(problems, &MISPProblem{
		source: "zzazz",
		output: 0,
	})

	problems = append(problems, &MISPProblem{
		source: "mbadm",
		output: 2,
	})

	problems = append(problems, &MISPProblem{
		source: "leetcode",
		output: 5,
	})

	problems = append(problems, &MISPProblem{
		source: "g",
		output: 0,
	})

	return &MISP{
		problems:    problems,
		currProblem: nil,
	}
}

var globalBest int

func (p *MISPProblem) calcMISP() int {
	size := len(p.source)
	globalBest = math.MaxInt32

	return p.makePalindrome(0, size-1, 0)
}

func (p *MISPProblem) makePalindrome(l, r, count int) int {
	for l < r {
		if p.source[l] == p.source[r] {
			l++
			r--
			continue
		}

		if count+1 >= globalBest {
			return math.MaxInt32
		}

		lInsrt := p.makePalindrome(l, r-1, count+1)
		rInsrt := p.makePalindrome(l+1, r, count+1)

		if lInsrt < rInsrt {
			return lInsrt
		}

		return rInsrt
	}

	if count < globalBest {
		globalBest = count
	}

	return count
}
