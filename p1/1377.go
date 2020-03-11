package p1

import (
	"fmt"
	"time"

	s "../shared"
)

// FPSProblems ...
type FPSProblems struct {
	set []*FPS
}

// Solve ...
func (p *FPSProblems) Solve() {
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

// FPS ...
type FPS struct {
	data   []int
	output int
}

// CreateFPS ...
func CreateFPS() s.Problem {
	set := make([]*FPS, 0, 4)

	set = append(set, &FPS{
		data:   []int{},
		output: 0,
	})

	return &FPSProblems{set}
}

func (p *FPS) solve() int {
	return 0
}
