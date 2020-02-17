package problems

import (
	"fmt"

	d "../../Utils"
)

// NPMS ...
type NPMS struct {
	problems    []*NPMSProblem
	currProblem *NPMSProblem
}

// Build ...
func (p *NPMS) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *NPMS) Run() {
	var prb *NPMSProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcNPMS(), prb.output)
			} else {
				prb.calcNPMS()
			}
		}
	}
}

// ResetGlobals ...
func (p *NPMS) ResetGlobals() {
}

// NPMSProblem ...
type NPMSProblem struct {
	source []string
	output []int
}

// CreateNPMS ...
func CreateNPMS() *NPMS {
	problems := make([]*NPMSProblem, 0)

	problems = append(problems, &NPMSProblem{
		source: []string{
			"E23", "2X2", "12S",
		},
		output: []int{7, 1},
	})

	problems = append(problems, &NPMSProblem{
		source: []string{
			"E12", "1X1", "21S",
		},
		output: []int{4, 2},
	})

	problems = append(problems, &NPMSProblem{
		source: []string{
			"E11", "XXX", "11S",
		},
		output: []int{0, 0},
	})

	return &NPMS{
		problems:    problems,
		currProblem: nil,
	}
}

var moveDirs = []int{-1, 0, -1, -1}

func (p *NPMSProblem) calcNPMS() []int {
	grid, scores, h, w := toGrid(p.source)
	results := []int{0, 0}

	stack := []*npmsNode{&npmsNode{
		x:     h - 1,
		y:     w - 1,
		score: 0,
	}}

	for len(stack) > 0 {
		next := make([]*npmsNode, 0, len(stack))

		for _, node := range stack {
			for i := 0; i < 3; i++ {
				x, y := node.x+moveDirs[i], node.y+moveDirs[i+1]
				if x < 0 || y < 0 {
					continue
				}

				if grid[x][y] < 0 {
					continue
				}

				sum := node.score + grid[x][y]
				if sum > scores[x][y] {
					scores[x][y] = sum
					next = append(next, &npmsNode{x: x, y: y, score: sum})
				}

				if x == 0 && y == 0 {
					if sum > results[0] {
						results[0] = sum
						results[1] = 1
					} else if sum == results[0] {
						results[1]++
					}
				}
			}
		}

		stack = next
	}

	return results
}

func toGrid(src []string) ([][]int, [][]int, int, int) {
	h, w := len(src), len(src[0])
	grid := make([][]int, h)
	scores := make([][]int, h)

	for i, val := range src {
		grid[i] = make([]int, w)
		scores[i] = make([]int, w)

		for j := 0; j < w; j++ {
			num := val[j] - '0'
			if num == 40 {
				grid[i][j] = -1
			} else if num <= 9 && num >= 0 {
				grid[i][j] = int(num)
			}
		}
	}

	return grid, scores, h, w
}

type npmsNode struct {
	x     int
	y     int
	score int
}
