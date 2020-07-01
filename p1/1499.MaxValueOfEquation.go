package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// XXXProblems ...
type XXXProblems struct {
	set []*XXX
}

// Solve ...
func (p *XXXProblems) Solve() {
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

// XXX ...
type XXX struct {
	data   []int
	output int
}

// CreateXXX ...
func CreateXXX() s.Problem {
	set := make([]*XXX, 0, 4)

	set = append(set, &XXX{
		data:   []int{},
		output: 0,
	})

	return &XXXProblems{set}
}

func (p *XXX) solve() int {
	return 0
}
