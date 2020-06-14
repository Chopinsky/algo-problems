package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// FPDProblems ...
type FPDProblems struct {
	set []*FPD
}

// Solve ...
func (p *FPDProblems) Solve() {
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

	fmt.Println("Algorithm took", time.Since(start))
}

// FPD ...
type FPD struct {
	data   []int
	output []int
}

// CreateFPD ...
func CreateFPD() s.Problem {
	set := make([]*FPD, 0, 4)

	set = append(set, &FPD{
		data:   []int{8, 4, 6, 2, 3},
		output: []int{4, 2, 4, 2, 3},
	})

	set = append(set, &FPD{
		data:   []int{1, 2, 3, 4, 5},
		output: []int{1, 2, 3, 4, 5},
	})

	set = append(set, &FPD{
		data:   []int{10, 1, 1, 6},
		output: []int{9, 0, 1, 6},
	})

	return &FPDProblems{set}
}

func (p *FPD) solve() []int {
	size := len(p.data)
	if size == 0 {
		return p.data
	}

	q := make([][]int, 0, size)
	var last, start int

	for i, val := range p.data {
		if i == 0 {
			q = append(q, []int{val, i})
			continue
		}

		last = len(q) - 1
		if val > q[last][0] {
			// nothing to get discount for
			q = append(q, []int{val, i})
			continue
		}

		for j, data := range q {
			if val <= data[0] {
				start = j
				break
			}
		}

		for j := start; j <= last; j++ {
			p.data[q[j][1]] -= val
		}

		q[start] = []int{val, i}
		q = q[:start+1]
	}

	return p.data
}
