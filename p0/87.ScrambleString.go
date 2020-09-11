package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// SSProblems ...
type SSProblems struct {
	set []*SS
}

// Solve ...
func (p *SSProblems) Solve() {
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

// SS ...
type SS struct {
	data   string
	target string
	output bool
}

// CreateSS ...
func CreateSS() s.Problem {
	set := make([]*SS, 0, 4)

	set = append(set, &SS{
		data:   "great",
		target: "rgeat",
		output: true,
	})

	set = append(set, &SS{
		data:   "abcde",
		target: "caebd",
		output: false,
	})

	set = append(set, &SS{
		data:   "abb",
		target: "bab",
		output: true,
	})

	return &SSProblems{set}
}

func (p *SS) solve() bool {
	return isScramble(p.data, p.target)
}

func isScramble(s1 string, s2 string) bool {
	if s1 == s2 {
		return true
	}

	size := len(s1)
	if size == 1 {
		return false
	}

	if size == 2 {
		return s1[0] == s2[1] && s1[1] == s2[0]
	}

	check := make(map[byte]int)
	for i := range s1 {
		check[s1[i]]++
		check[s2[i]]--
	}

	for _, v := range check {
		if v != 0 {
			return false
		}
	}

	// partisitioning
	for i := 1; i < size; i++ {
		if isScramble(s1[:i], s2[:i]) && isScramble(s1[i:], s2[i:]) {
			return true
		}

		if isScramble(s1[:i], s2[size-i:]) && isScramble(s1[i:], s2[:size-i]) {
			return true
		}
	}

	return false
}
