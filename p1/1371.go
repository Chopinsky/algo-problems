package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// FLSCVProblems ...
type FLSCVProblems struct {
	set []*FLSCV
}

// Solve ...
func (p *FLSCVProblems) Solve() {
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

// FLSCV ...
type FLSCV struct {
	data   string
	output int
}

// CreateFLSCV ...
func CreateFLSCV() s.Problem {
	set := make([]*FLSCV, 0, 4)

	set = append(set, &FLSCV{
		data:   "eleetminicoworoep",
		output: 13,
	})

	set = append(set, &FLSCV{
		data:   "leetcodeisgreat",
		output: 5,
	})

	set = append(set, &FLSCV{
		data:   "bcbcbc",
		output: 6,
	})

	set = append(set, &FLSCV{
		data:   "aeiou",
		output: 0,
	})

	return &FLSCVProblems{set}
}

func (p *FLSCV) solve() int {
	size := len(p.data)
	m := make(map[int]int, size)

	posMap := map[rune]uint{
		'a': 0,
		'e': 1,
		'i': 2,
		'o': 3,
		'u': 4,
	}

	// state is the prefix sum of the number of vowels
	state, best, betweenVowels := 0, 0, 0

	for i, char := range p.data {
		if pos, ok := posMap[char]; ok {
			// we're at the end of a persisting state, calculate how many
			// characters are in this substring
			if last, ok := m[state]; ok {
				l := i - last - 1

				// special cases for all-even state, where the state-changer
				// char shall be included (vs. excluded for other cases)
				if state == 0 {
					l++
				}

				if l > best {
					best = l
				}
			}

			betweenVowels = 0
			state ^= 1 << pos

			if _, ok := m[state]; !ok {
				m[state] = i
			}
		} else {
			if i == 0 {
				m[state] = 0
			}

			betweenVowels++
			if betweenVowels > best {
				best = betweenVowels
			}
		}
	}

	return best
}
