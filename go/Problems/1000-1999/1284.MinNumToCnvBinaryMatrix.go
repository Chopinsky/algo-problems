package problems

import (
	"fmt"

	d "../../Utils"
)

// MNCBM ...
type MNCBM struct {
	problems    []*MNCBMProblem
	currProblem *MNCBMProblem
}

// MNCBMProblem ...
type MNCBMProblem struct {
	source [][]int
	output int
}

// CreateMNCBM ...
func CreateMNCBM() *MNCBM {
	problems := make([]*MNCBMProblem, 0)

	problems = append(problems, &MNCBMProblem{
		source: [][]int{
			{0, 0},
			{0, 1},
		},
		output: 3,
	})

	problems = append(problems, &MNCBMProblem{
		source: [][]int{
			{0},
		},
		output: 0,
	})

	problems = append(problems, &MNCBMProblem{
		source: [][]int{
			{1, 1, 1},
			{1, 0, 1},
			{0, 0, 0},
		},
		output: 6,
	})

	problems = append(problems, &MNCBMProblem{
		source: [][]int{
			{1, 0, 0},
			{1, 0, 0},
		},
		output: -1,
	})

	return &MNCBM{
		problems:    problems,
		currProblem: nil,
	}
}

// Build ...
func (p *MNCBM) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *MNCBM) Run() {
	var prb *MNCBMProblem

	num := len(p.problems)

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < num; i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case", i, "<<<")
				d.Output(prb.calcMNCBM(), prb.output)
			} else {
				prb.calcMNCBM()
			}
		}
	}
}

var matrixCache map[int]struct{}

// ResetGlobals ...
func (p *MNCBM) ResetGlobals() {
	matrixCache = make(map[int]struct{}, 1<<9)
}

func (p *MNCBMProblem) calcMNCBM() int {
	src, h, w := 0, len(p.source), len(p.source[0])

	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if p.source[i][j] == 1 {
				src |= 1 << (uint)(i*w+j)
			}
		}
	}

	if d.DEBUG {
		printBinary(src, 9)
	}

	if src == 0 {
		return 0
	}

	matrixCache[src] = empty
	stack := []int{src}
	moves := 1

	for len(stack) > 0 {
		if d.DEBUG {
			fmt.Println(stack)
		}

		nextMoves := make([]int, 0, 8)

		// iterate all matrix setups, and try flip 1 node for each position
		for _, val := range stack {
			for i := 0; i < h; i++ {
				for j := 0; j < w; j++ {
					nextVal := flip(val, i, j, h, w)

					if nextVal == 0 {
						return moves
					}

					if _, ok := matrixCache[nextVal]; ok {
						continue
					}

					// push the next setup to the stack, and mark it as visited
					nextMoves = append(nextMoves, nextVal)
					matrixCache[nextVal] = empty
				}
			}
		}

		stack = nextMoves
		moves++
	}

	return -1
}

func flip(src int, i, j, h, w int) int {
	if i >= h || j >= w {
		return src
	}

	src = flipOneDigit(src, i*w+j)

	if i+1 < h {
		src = flipOneDigit(src, (i+1)*w+j)
	}

	if j-1 >= 0 {
		src = flipOneDigit(src, i*w+j-1)
	}

	if i-1 >= 0 {
		src = flipOneDigit(src, (i-1)*w+j)
	}

	if j+1 < w {
		src = flipOneDigit(src, i*w+j+1)
	}

	return src
}

func flipOneDigit(src int, pos int) int {
	return src ^ (1 << (uint)(pos))
}
