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
	output int
}

// CreateFPD ...
func CreateFPD() s.Problem {
	set := make([]*FPD, 0, 4)

	set = append(set, &FPD{
		data:   []int{},
		output: 0,
	})

	return &FPDProblems{set}
}

func (p *FPD) solve() int {
	return 0
}
