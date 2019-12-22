package problems

import (
	"fmt"

	d "../../Utils"
)

// MSW ...
type MSW struct {
	problems    []*MSWProblem
	currProblem *MSWProblem
}

// Build ...
func (p *MSW) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *MSW) Run() {
	var prb *MSWProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcMSW(), prb.output)
			} else {
				prb.calcMSW()
			}
		}
	}
}

// ResetGlobals ...
func (p *MSW) ResetGlobals() {
}

// MSWProblem ...
type MSWProblem struct {
	source    [][]int
	threshold int
	output    int
}

// CreateMSW ...
func CreateMSW() *MSW {
	problems := make([]*MSWProblem, 0)

	problems = append(problems, &MSWProblem{
		source: [][]int{
			{1, 1, 3, 2, 4, 3, 2},
			{1, 1, 3, 2, 4, 3, 2},
			{1, 1, 3, 2, 4, 3, 2},
		},
		threshold: 4,
		output:    2,
	})

	problems = append(problems, &MSWProblem{
		source: [][]int{
			{2, 2, 2, 2, 2},
			{2, 2, 2, 2, 2},
			{2, 2, 2, 2, 2},
		},
		threshold: 1,
		output:    0,
	})

	return &MSW{
		problems:    problems,
		currProblem: nil,
	}
}

type square struct {
	x   int
	y   int
	sum int
}

func (p *MSWProblem) calcMSW() int {
	curr := p.source
	h, w := len(p.source), len(p.source[0])

	if h == 1 || w == 1 {
		return 1
	}

	row := makeArr(h, w)
	col := makeArr(h, w)
	stack := []*square{}
	valid := false

	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if j > 0 {
				row[i][j] = row[i][j-1] + curr[i][j]
			} else {
				row[i][0] = curr[i][0]
			}

			if i > 0 {
				col[i][j] = col[i-1][j] + curr[i][j]
			} else {
				col[0][j] = curr[0][j]
			}

			valid = valid || (curr[i][j] <= p.threshold)

			if curr[i][j] < p.threshold && i+1 < h && j+1 < w {
				stack = append(stack, &square{
					x:   i,
					y:   j,
					sum: curr[i][j],
				})
			}
		}
	}

	if !valid {
		return 0
	}

	i := 1
	for len(stack) > 0 {
		next := []*square{}
		valid = false

		for _, anchor := range stack {
			x0, y0 := anchor.x, anchor.y
			x1, y1 := x0+i, y0+i

			anchor.sum +=
				calcSum(row, x0, y0, x0, y1) + calcSum(col, x0, y0, x1, y0) - curr[x1][y1]

			valid = valid || anchor.sum <= p.threshold

			if anchor.sum < p.threshold && anchor.x+i+1 < h && anchor.y+i+1 < w {
				next = append(next, anchor)
			}
		}

		i++
		stack = next
	}

	return i
}

func (p *MSWProblem) calcMSW1() int {
	curr := p.source
	h, w := len(curr), len(curr[0])
	found := false

	row := makeArr(h, w)
	col := makeArr(h, w)

	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if j > 0 {
				row[i][j] = row[i][j-1] + curr[i][j]
			} else {
				row[i][0] = curr[i][0]
			}

			if i > 0 {
				col[i][j] = col[i-1][j] + curr[i][j]
			} else {
				col[0][j] = curr[0][j]
			}

			found = found || (curr[i][j] <= p.threshold)
		}
	}

	// fmt.Println(row, col)

	if !found {
		return 0
	}

	i := 1
	for i < h {
		next := makeArr(h, w)
		found = false

		for j := 0; j < h-i; j++ {
			for k := 0; k < w-i; k++ {
				j0, k0 := j+i, k+i

				// fmt.Println(i, j, k, j0, k0)

				a := calcSum(row, j, k, j, k0)
				b := calcSum(col, j, k, j0, k)

				next[j][k] = curr[j][k] + a + b - p.source[j0][k0]

				found = found || next[j][k] <= p.threshold
			}
		}

		// fmt.Println(found, next, p.source)

		if !found {
			break
		}

		i++
		curr = next
	}

	return i
}

func calcSum(src [][]int, i0, j0, i1, j1 int) int {
	if i0 == 0 || j0 == 0 {
		return src[i1][j1]
	}

	if i0 == i1 {
		j0--
	} else {
		i0--
	}

	return src[i1][j1] - src[i0][j0]
}

func makeArr(h, w int) [][]int {
	arr := make([][]int, h)
	for i := 0; i < h; i++ {
		arr[i] = make([]int, w)
	}

	return arr
}
