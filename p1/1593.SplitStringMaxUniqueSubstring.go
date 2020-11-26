package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// SSMUSProblems ...
type SSMUSProblems struct {
	set []*SSMUS
}

// Solve ...
func (p *SSMUSProblems) Solve() {
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

// SSMUS ...
type SSMUS struct {
	data   string
	output int
}

// CreateSSMUS ...
func CreateSSMUS() s.Problem {
	set := make([]*SSMUS, 0, 4)

	set = append(set, &SSMUS{
		data:   "aa",
		output: 1,
	})

	set = append(set, &SSMUS{
		data:   "aba",
		output: 2,
	})

	set = append(set, &SSMUS{
		data:   "abaabccc",
		output: 5,
	})

	set = append(set, &SSMUS{
		data:   "abaabcccddeeeffs",
		output: 11,
	})

	return &SSMUSProblems{set}
}

func (p *SSMUS) solve() int {
	store := make(map[string]bool)
	return searchSubstr(p.data, store, 0)
}

func searchSubstr(src string, store map[string]bool, count int) int {
	size := len(src)
	if size == 0 {
		return count
	}

	best := 0
	for i := 0; i < size; i++ {
		if store[src[:i+1]] {
			continue
		}

		store[src[:i+1]] = true
		nextCount := searchSubstr(src[i+1:], store, count+1)

		if nextCount > 0 && nextCount > best {
			best = nextCount
		}

		store[src[:i+1]] = false
	}

	return best
}
