package problems

import (
	"fmt"

	d "../../Utils"
)

// LPS ...
type LPS struct {
	problems    []*LPSProblem
	currProblem *LPSProblem
}

// Build ...
func (p *LPS) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *LPS) Run() {
	var prb *LPSProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcLPS(), prb.output)
			} else {
				prb.calcLPS()
			}
		}
	}
}

var pCache map[string]bool

// ResetGlobals ...
func (p *LPS) ResetGlobals() {
	pCache = make(map[string]bool, 255)
}

// LPSProblem ...
type LPSProblem struct {
	source string
	output string
}

// CreateLPS ...
func CreateLPS() *LPS {
	problems := make([]*LPSProblem, 0)

	problems = append(problems, &LPSProblem{
		source: "babad",
		output: "bab",
	})

	problems = append(problems, &LPSProblem{
		source: "cbbd",
		output: "bb",
	})

	return &LPS{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *LPSProblem) calcLPS() string {
	longest, target := 1, p.source[0:1]

	for i := 1; i < len(p.source); i++ {
		for j := 0; j < i; j++ {
			if i+1-j <= longest {
				break
			}

			if isStrPalindrome(p.source[j : i+1]) {
				longest = i + 1 - j
				target = p.source[j : i+1]

				break
			}
		}
	}

	if d.DEBUG {
		fmt.Println("the longest substring is: '", target, "' ; and has length:", longest)
	}

	return target
}

func isStrPalindrome(s string) bool {
	if res, ok := pCache[s]; ok {
		return res
	}

	size := len(s)
	res := true

	for i := 0; i < size/2; i++ {
		if s[i] != s[size-i-1] {
			res = false
			break
		}
	}

	pCache[s] = res

	return res
}
