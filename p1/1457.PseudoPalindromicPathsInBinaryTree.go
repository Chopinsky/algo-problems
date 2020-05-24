package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// PPPBTProblems ...
type PPPBTProblems struct {
	set []*PPPBT
}

// Solve ...
func (p *PPPBTProblems) Solve() {
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

// PPPBT ...
type PPPBT struct {
	data   []int
	output int
}

// CreatePPPBT ...
func CreatePPPBT() s.Problem {
	set := make([]*PPPBT, 0, 4)

	set = append(set, &PPPBT{
		data:   []int{},
		output: 0,
	})

	return &PPPBTProblems{set}
}

func (p *PPPBT) solve() int {
	return 0
}
