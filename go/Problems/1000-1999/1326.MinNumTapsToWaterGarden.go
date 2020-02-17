package problems

import (
	"fmt"

	d "../../Utils"
)

// MNTWG ...
type MNTWG struct {
	problems    []*MNTWGProblem
	currProblem *MNTWGProblem
}

// Build ...
func (p *MNTWG) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *MNTWG) Run() {
	var prb *MNTWGProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcMNTWG(), prb.output)
			} else {
				// prb.calcMNTWG()
			}
		}
	}
}

// ResetGlobals ...
func (p *MNTWG) ResetGlobals() {
}

// MNTWGProblem ...
type MNTWGProblem struct {
	source []int
	size   int
	output int
}

// CreateMNTWG ...
func CreateMNTWG() *MNTWG {
	problems := make([]*MNTWGProblem, 0)

	problems = append(problems, &MNTWGProblem{
		source: []int{3, 4, 1, 1, 0, 0},
		size:   5,
		output: 1,
	})

	problems = append(problems, &MNTWGProblem{
		source: []int{0, 0, 0, 0},
		size:   3,
		output: -1,
	})

	problems = append(problems, &MNTWGProblem{
		source: []int{1, 2, 1, 0, 2, 1, 0, 1},
		size:   7,
		output: 3,
	})

	problems = append(problems, &MNTWGProblem{
		source: []int{4, 0, 0, 0, 0, 0, 0, 0, 4},
		size:   8,
		output: 2,
	})

	problems = append(problems, &MNTWGProblem{
		source: []int{4, 0, 0, 0, 4, 0, 0, 0, 4},
		size:   8,
		output: 1,
	})

	return &MNTWG{
		problems:    problems,
		currProblem: nil,
	}
}

type tap struct {
	pos     int
	rng     int
	visited bool
}

var taps []*tap

func (p *MNTWGProblem) calcMNTWG() int {
	taps = make([]*tap, 0, p.size+1)
	rawSum := 0

	for i := 0; i < p.size+1; i++ {
		if p.source[i] > 0 {
			rng := 1

			if i-p.source[i] >= 0 {
				rng += p.source[i]
			} else {
				rng += i
			}

			if i+p.source[i] <= p.size {
				rng += p.source[i]
			} else {
				rng += p.size - i
			}

			rawSum += rng

			taps = append(taps, &tap{pos: i, rng: rng})
		}
	}

	if d.DEBUG {
		for _, val := range taps {
			fmt.Println(val.rng)
		}
	}

	if len(taps) == 0 || rawSum < p.size+1 {
		// early termination, not gonna happen
		return -1
	}

	return p.count(0, p.size, -1, p.size+1)
}

func (p *MNTWGProblem) count(l, r, lStart, rStart int) int {
	if l > r {
		return -1
	}

	if d.DEBUG {
		fmt.Println(l, r, lStart, rStart)
	}

	if l == r {
		if p.source[l] > 0 {
			return 1
		}

		return p.walkBack(l, r, lStart, rStart)
	}

	center, rng := p.findCenter(l, r)

	if center != nil {
		// if opening the center tap will cover the entire range, we're done
		if rng >= (r - l + 1) {
			return 1
		}

		count := 1
		lBound, rBound := center.pos-p.source[center.pos]-1, center.pos+p.source[center.pos]+1

		// fmt.Println(l, r, center.pos, lBound, rBound)

		if lBound >= l {
			lCount := p.count(l, lBound, lStart, center.pos)

			if d.DEBUG {
				fmt.Println(center.pos, " (left) ", lCount)
			}

			if lCount == -1 {
				return -1
			}

			count += lCount
		}

		if rBound <= r {
			rCount := p.count(rBound, r, center.pos, rStart)

			if d.DEBUG {
				fmt.Println(center.pos, " (right) ", rCount)
			}

			if rCount == -1 {
				return -1
			}

			count += rCount
		}

		return count
	}

	return p.walkBack(l, r, lStart, rStart)
}

func (p *MNTWGProblem) walkBack(l, r, lStart, rStart int) int {
	lPos, rPos := l-1, r+1
	lBound, rBound := lPos, rPos

	for lPos > lStart {
		pos := lPos + p.source[lPos]

		if pos >= r {
			return 1
		}

		if pos > lBound {
			lBound = pos
		}

		lPos--
	}

	for rPos < rStart {
		pos := rPos - p.source[rPos]

		if pos <= l {
			return 1
		}

		if pos < rBound {
			rBound = pos
		}

		rPos++
	}

	if lBound >= rBound {
		return 2
	}

	return -1
}

func (p *MNTWGProblem) findCenter(l, r int) (*tap, int) {
	var center *tap
	rng := 0

	for _, val := range taps {
		if val.visited || val.pos < l {
			continue
		}

		if val.pos > r {
			break
		}

		currRng := p.getRange(val.pos, l, r)

		if center != nil {
			if currRng > rng || (currRng == rng && val.pos > center.pos) {
				center = val
				rng = currRng
			}
		} else {
			center = val
			rng = currRng
		}
	}

	return center, rng
}

func (p *MNTWGProblem) getRange(i, l, r int) int {
	rng := 1

	if i-p.source[i] >= l {
		rng += p.source[i]
	} else {
		rng += i - l
	}

	if i+p.source[i] <= r {
		rng += p.source[i]
	} else {
		rng += r - i
	}

	return rng
}
