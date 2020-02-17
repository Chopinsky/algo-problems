package problems

import (
	"fmt"

	d "../../Utils"
)

// XORQ ...
type XORQ struct {
	problems    []*XORQProblem
	currProblem *XORQProblem
}

// Build ...
func (p *XORQ) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *XORQ) Run() {
	var prb *XORQProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcXORQ(), prb.output)
			} else {
				prb.calcXORQ()
			}
		}
	}
}

// ResetGlobals ...
func (p *XORQ) ResetGlobals() {
}

// XORQProblem ...
type XORQProblem struct {
	source  []int
	queries [][]int
	output  []int
}

// CreateXORQ ...
func CreateXORQ() *XORQ {
	problems := make([]*XORQProblem, 0)

	problems = append(problems, &XORQProblem{
		source: []int{1, 3, 4, 8},
		queries: [][]int{
			{0, 1},
			{1, 2},
			{0, 3},
			{3, 3},
		},
		output: []int{2, 7, 14, 8},
	})

	problems = append(problems, &XORQProblem{
		source: []int{4, 8, 2, 10},
		queries: [][]int{
			{2, 3},
			{1, 3},
			{0, 0},
			{0, 3},
		},
		output: []int{8, 0, 4, 4},
	})

	return &XORQ{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *XORQProblem) calcXORQ() []int {
	xor := make([]int, 0, len(p.source))
	xor = append(xor, p.source[0])

	for i := 1; i < len(p.source); i++ {
		val := p.source[i] ^ xor[i-1]
		xor = append(xor, val)
	}

	results := make([]int, 0, len(p.queries))
	for i := 0; i < len(p.queries); i++ {
		results = append(results, xorVals(p.source, xor, p.queries[i][0], p.queries[i][1]))
	}

	return results
}

func xorVals(src, xor []int, i, j int) int {
	if i == j {
		return src[i]
	}

	if i == 0 {
		return xor[j]
	}

	return xor[j] ^ xor[i-1]
}
