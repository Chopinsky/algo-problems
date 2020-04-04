package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// CNTProblems ...
type CNTProblems struct {
	set []*CNT
}

// Solve ...
func (p *CNTProblems) Solve() {
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

// CNT ...
type CNT struct {
	data   []int
	output int
}

// CreateCNT ...
func CreateCNT() s.Problem {
	set := make([]*CNT, 0, 4)

	set = append(set, &CNT{
		data:   []int{},
		output: 0,
	})

	return &CNTProblems{set}
}

func (p *CNT) solve() int {
	return 0
}
