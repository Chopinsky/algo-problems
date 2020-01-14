package problems

import (
	"fmt"

	d "../../Utils"
)

// MDTW ...
type MDTW struct {
	problems    []*MDTWProblem
	currProblem *MDTWProblem
}

// Build ...
func (p *MDTW) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *MDTW) Run() {
	var prb *MDTWProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcMDTW(), prb.output)
			} else {
				// prb.calcMDTW()
			}
		}
	}
}

// ResetGlobals ...
func (p *MDTW) ResetGlobals() {
}

// MDTWProblem ...
type MDTWProblem struct {
	source string
	output int
}

var distCache map[int]uint
var mem [][][]int

// CreateMDTW ...
func CreateMDTW() *MDTW {
	problems := make([]*MDTWProblem, 0)

	problems = append(problems, &MDTWProblem{
		source: "cake",
		output: 3,
	})

	problems = append(problems, &MDTWProblem{
		source: "happy",
		output: 6,
	})

	problems = append(problems, &MDTWProblem{
		source: "new",
		output: 3,
	})

	problems = append(problems, &MDTWProblem{
		source: "year",
		output: 7,
	})

	problems = append(problems, &MDTWProblem{
		source: "yearasdlkjhasdjkfhglqkwehyjtlkandslkgnaldwqetjkqbnlkmbnxclasjdhgqewrthkjhbzfga",
		output: 159,
	})

	return &MDTW{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *MDTWProblem) calcMDTW() int {
	distCache = make(map[int]uint)
	size := len(p.source)

	mem = make([][][]int, size)
	for i := 0; i < size; i++ {
		mem[i] = make([][]int, 27)
		for j := 0; j < 27; j++ {
			mem[i][j] = make([]int, 27)
		}
	}

	// return p.calcDist(1, len(p.source), 0, -1, 0)
	// return p.calcDist2()
	// return p.calcDist3(size, 0, 26, 26)

	return p.calcDist4()
}

func (p *MDTWProblem) calcDist(i, size, left, right int, score uint) uint {
	lScore := p.getDist(left, i)
	rScore := p.getDist(right, i)

	if i == size-1 {
		if lScore < rScore {
			return score + lScore
		}

		return score + rScore
	}

	lScore = p.calcDist(i+1, size, i, right, score+lScore)
	rScore = p.calcDist(i+1, size, left, i, score+rScore)

	if lScore < rScore {
		return lScore
	}

	return rScore
}

type score struct {
	pos   int
	left  int
	right int
	score uint
}

func (p *MDTWProblem) calcDist2() uint {
	stack, size := make([]*score, 0, 1<<8), len(p.source)

	stack = append(stack, &score{
		pos:   1,
		left:  0,
		right: -1,
		score: 0,
	})

	bestScore := uint(1 << 16)
	var curr *score
	var lScore, rScore uint

	for len(stack) > 0 {
		curr, stack = stack[0], stack[1:]

		lScore = p.getDist(curr.left, curr.pos) + curr.score
		rScore = p.getDist(curr.right, curr.pos) + curr.score

		if lScore >= bestScore && rScore >= bestScore {
			continue
		}

		if curr.pos == size-1 {
			if lScore < bestScore {
				bestScore = lScore
			}

			if rScore < bestScore {
				bestScore = rScore
			}

			continue
		}

		// if right finger types the current char
		if rScore < bestScore {
			next := &score{
				left:  curr.left,
				right: curr.pos,
				pos:   curr.pos + 1,
				score: rScore,
			}

			stack = append(stack, next)
		}

		// if left finger types the current char
		if lScore < bestScore {
			curr.left = curr.pos
			curr.pos++
			curr.score = lScore
			stack = append(stack, curr)
		}
	}

	return bestScore
}

/*
 * ???
func (p *MDTWProblem) calcDist3(size, i, l, r int) int {
	if i == size {
		return 0
	}

	if mem[i][l][r] > 0 {
		return mem[i][l][r]
	}

	currChar := int(p.source[i] - charA)

	lScore := p.calcDist3(size, i+1, currChar, r) + cost(l, currChar)
	rScore := p.calcDist3(size, i+1, l, currChar) + cost(r, currChar)

	if lScore < rScore {
		mem[i][l][r] = lScore
	}

	mem[i][l][r] = rScore

	return mem[i][l][r]
}
*/

func (p *MDTWProblem) calcDist4() int {
	size := len(p.source)

	dp := make([][]int, size+1)
	for i := 0; i < size+1; i++ {
		dp[i] = make([]int, 27)
		for j := 0; j <= 26; j++ {
			dp[i][j] = 1<<12 - 1
		}
	}

	dp[0][26] = 0

	bestScore := 1<<16 - 1
	var last, curr int

	for i := 0; i < size; i++ {
		if i > 0 {
			last = int(p.source[i-1] - charA)
		} else {
			last = 26
		}

		curr = int(p.source[i] - charA)

		for j := 0; j <= 26; j++ {
			j0 := dp[i][j] + cost(last, curr)
			j1 := dp[i][j] + cost(j, curr)

			if j0 < dp[i+1][j] {
				dp[i+1][j] = j0
			}

			if j1 < dp[i+1][last] {
				dp[i+1][last] = j1
			}

			if i == size-1 {
				if j0 < bestScore {
					bestScore = j0
				}

				if j1 < bestScore {
					bestScore = j1
				}
			}
		}
	}

	// fmt.Println(dp)

	return bestScore
}

func (p *MDTWProblem) getDist(i, j int) uint {
	if i == -1 {
		return 0
	}

	a, b := int(p.source[i]-charA), int(p.source[j]-charA)

	return getCost(a, b)
}

func cost(a, b int) int {
	if a == 26 {
		return 0
	}

	p1 := a/6 - b/6
	p2 := a%6 - b%6

	if p1 < 0 {
		p1 *= -1
	}

	if p2 < 0 {
		p2 *= -1
	}

	return p1 + p2
}

func getCost(a, b int) uint {
	if a == 26 || b == 26 {
		return 0
	}

	key := a*26 + b

	if val, ok := distCache[key]; ok {
		return val
	}

	ax, ay := getCharPos(a)
	bx, by := getCharPos(b)

	if ax > bx {
		ax, bx = bx, ax
	}

	if ay > by {
		ay, by = by, ay
	}

	res := uint(bx - ax + by - ay)
	distCache[key] = res

	return res
}

func getCharPos(ch int) (int, int) {
	return ch / 6, ch % 6
}
