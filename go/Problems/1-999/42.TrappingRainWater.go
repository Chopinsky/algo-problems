package problems

import (
	"fmt"

	d "../../Utils"
)

// TRW ...
type TRW struct {
	problems    []*TRWProblem
	currProblem *TRWProblem
}

// Build ...
func (p *TRW) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *TRW) Run() {
	var prb *TRWProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcTRW(), prb.output)
			} else {
				prb.calcTRW()
			}
		}
	}
}

// ResetGlobals ...
func (p *TRW) ResetGlobals() {
}

// TRWProblem ...
type TRWProblem struct {
	source []int
	output int
}

// CreateTRW ...
func CreateTRW() *TRW {
	problems := make([]*TRWProblem, 0)

	problems = append(problems, &TRWProblem{
		source: []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1},
		output: 6,
	})

	return &TRW{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *TRWProblem) calcTRW() int {
	src, size := p.source, len(p.source)
	dp := make([]int, size)

	dp[0] = -1
	count := 0

	for i := 1; i < size; i++ {
		if src[i] == src[i-1] {
			dp[i] = dp[i-1]
			continue
		}

		if src[i] > src[i-1] {
			otherWall, height := lookback(src, dp, i)

			if d.DEBUG {
				fmt.Println("@", i, otherWall, height)
			}

			if otherWall < 0 {
				dp[i] = -1
				continue
			}

			count += (i - 1 - otherWall) * (height - src[i-1])

			if src[otherWall] > src[i] {
				dp[i] = otherWall
			} else if src[otherWall] == src[i] {
				dp[i] = dp[otherWall]
			} else {
				dp[i] = -1
			}

			continue
		}

		// src[i] < src[i-1]
		dp[i] = i - 1
	}

	if !d.DEBUG {
		fmt.Println(dp)
	}

	return count
}

func lookback(src, dp []int, origin int) (int, int) {
	next := dp[origin-1]
	upper := src[origin]

	for next >= 0 {
		if src[next] >= upper {
			return next, upper
		}

		if dp[next] < 0 {
			return next, src[next]
		}

		next = dp[next]
	}

	if next < 0 {
		return next, -1
	}

	return next, src[next]
}

func (p *TRWProblem) fakeCalc() int {
	// store := make(map[int][]int)
	// walls := make([]int, 0, size)

	storeMode := false
	count, pos, size := 0, 1, len(p.source)

	for pos < size {
		// non-store mode
		if !storeMode && p.source[pos] < p.source[pos-1] {
			pos--
			storeMode = true
			continue
		}

		// store mode

		pos++
	}

	for pos < size {

	}

	return count
}
