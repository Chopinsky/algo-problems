package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// LSADOEProblems ...
type LSADOEProblems struct {
	set []*LSADOE
}

// Solve ...
func (p *LSADOEProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm finished in:", time.Since(start))
}

// LSADOE ...
type LSADOE struct {
	data   []int
	output int
}

// CreateLSADOE ...
func CreateLSADOE() s.Problem {
	set := make([]*LSADOE, 0, 4)

	set = append(set, &LSADOE{
		data:   []int{1, 1, 0, 1},
		output: 3,
	})

	set = append(set, &LSADOE{
		data:   []int{0, 1, 1, 1, 0, 1, 1, 0, 1},
		output: 5,
	})

	set = append(set, &LSADOE{
		data:   []int{1, 1, 1},
		output: 2,
	})

	set = append(set, &LSADOE{
		data:   []int{1, 1, 0, 0, 1, 1, 1, 0, 1},
		output: 4,
	})

	set = append(set, &LSADOE{
		data:   []int{0, 0, 0},
		output: 0,
	})

	return &LSADOEProblems{set}
}

func (p *LSADOE) solve() int {
	last := -1
	lc, cc := 0, 0
	best := 0

	for i, val := range p.data {
		if val == 1 {
			cc++
			continue
		}

		if last >= 0 {
			if lc+cc > best {
				best = lc + cc
			}
		} else {
			last = i
		}

		lc, cc = cc, 0
	}

	if last < 0 {
		// there isn't a 0 in the array, but we must delete a 1
		return len(p.data) - 1
	}

	if lc+cc > best {
		best = lc + cc
	}

	return best
}
