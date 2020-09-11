package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// RSPProblems ...
type RSPProblems struct {
	set []*RSP
}

// Solve ...
func (p *RSPProblems) Solve() {
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

// RSP ...
type RSP struct {
	data   string
	output bool
}

// CreateRSP ...
func CreateRSP() s.Problem {
	set := make([]*RSP, 0, 4)

	set = append(set, &RSP{
		data:   "abcabcabcabc",
		output: true,
	})

	return &RSPProblems{set}
}

func (p *RSP) solve() bool {
	s := p.data
	size, j := len(s), 0
	jump := make([]int, size)

	for i := 1; i < size; i++ {
		for j > 0 && s[i] != s[j] {
			j = jump[j-1]
		}

		if s[i] == s[j] {
			j++
		}

		jump[i] = j
	}

	last := jump[size-1]

	return last != 0 && (size%(size-last)) == 0
}
