package problems

import (
	"fmt"

	d "../../Utils"
)

// SPG ...
type SPG struct {
	problems    []*SPGProblem
	currProblem *SPGProblem
}

// Build ...
func (p *SPG) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *SPG) Run() {
	var prb *SPGProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcSPG(), prb.output)
			} else {
				prb.calcSPG()
			}
		}
	}
}

// ResetGlobals ...
func (p *SPG) ResetGlobals() {
}

// SPGProblem ...
type SPGProblem struct {
	source [][]int
	k      int
	output int
}

// CreateSPG ...
func CreateSPG() *SPG {
	problems := make([]*SPGProblem, 0)

	problems = append(problems, &SPGProblem{
		source: [][]int{
			{0, 0, 0},
			{1, 1, 0},
			{0, 0, 0},
			{0, 1, 1},
			{0, 0, 0},
		},
		k:      1,
		output: 6,
	})

	problems = append(problems, &SPGProblem{
		source: [][]int{
			{0, 1, 1},
			{1, 1, 1},
			{1, 0, 0},
		},
		k:      1,
		output: -1,
	})

	return &SPG{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *SPGProblem) calcSPG() int {
	h, w := len(p.source), len(p.source[0])

	dp := make([][]int, h)
	for i := 0; i < h; i++ {
		dp[i] = make([]int, w)

		for j := 0; j < w; j++ {
			dp[i][j] = -1
		}
	}

	stack := []*posInfo{&posInfo{
		x: 0,
		y: 0,
		k: p.k,
	}}

	steps := 0

	for len(stack) > 0 {
		temp := make([]*posInfo, 0, 2*len(stack))
		steps++

		for _, pos := range stack {
			for i := 0; i < 4; i++ {
				x, y := pos.x+dir[i], pos.y+dir[i+1]

				if x < 0 || y < 0 || x >= h || y >= w {
					continue
				}

				if p.source[x][y] == 1 && pos.k == 0 {
					continue
				}

				if x == h-1 && y == w-1 {
					return steps
				}

				nextK := pos.k - p.source[x][y]

				if nextK <= dp[x][y] {
					continue
				}

				dp[x][y] = nextK

				temp = append(temp, &posInfo{
					x: x,
					y: y,
					k: nextK,
				})
			}
		}

		stack = temp
	}

	return -1
}

type posInfo struct {
	x int
	y int
	k int
}
