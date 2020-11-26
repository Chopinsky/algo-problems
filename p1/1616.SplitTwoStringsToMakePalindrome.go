package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// STSMPProblems ...
type STSMPProblems struct {
	set []*STSMP
}

// Solve ...
func (p *STSMPProblems) Solve() {
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

// STSMP ...
type STSMP struct {
	a      string
	b      string
	output bool
}

// CreateSTSMP ...
func CreateSTSMP() s.Problem {
	set := make([]*STSMP, 0, 4)

	set = append(set, &STSMP{
		a:      "x",
		b:      "y",
		output: true,
	})

	set = append(set, &STSMP{
		a:      "abdef",
		b:      "fecab",
		output: true,
	})

	set = append(set, &STSMP{
		a:      "ulacfd",
		b:      "jizalu",
		output: true,
	})

	set = append(set, &STSMP{
		a:      "xbdef",
		b:      "xecab",
		output: false,
	})

	return &STSMPProblems{set}
}

func (p *STSMP) solve() bool {
	a, b := p.a, p.b
	la, lb := len(a), len(b)

	// not covered case
	if la != lb {
		return false
	}

	if la <= 1 || isPalindrome(a, 0, la-1) || isPalindrome(b, 0, lb-1) {
		return true
	}

	return verify(a, b, la) || verify(b, a, lb)
}

func verify(src, tgt string, size int) bool {
	si, ti := 0, size-1

	for si < ti && si < size && ti >= 0 {
		if src[si] != tgt[ti] {
			break
		}

		si++
		ti--
	}

	// no match for this pair
	if si == 0 || ti == size-1 {
		return false
	}

	// range overlapped, done
	if si == ti || si == ti+1 {
		return true
	}

	// determine if src's middle section is palindrome as well
	for si >= 0 && ti < size {
		if isPalindrome(src, si, ti) {
			return true
		}

		si--
		ti++
	}

	return false
}

func isPalindrome(s string, i, j int) bool {
	if i > j {
		return false
	}

	if i == j || len(s) <= 1 {
		return true
	}

	for i <= j {
		if s[i] != s[j] {
			return false
		}

		i++
		j--
	}

	return true
}
