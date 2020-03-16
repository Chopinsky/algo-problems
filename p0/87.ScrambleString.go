package p0

import (
	"fmt"
	"time"

	s "../shared"
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

	return &SSProblems{set}
}

func (p *SS) solve() bool {
	src, tgt := p.data, p.target
	size := len(p.data)

	i, j := 0, size-1
	for i < j {
		canContinue := false

		if src[i] == tgt[i] {
			i++
			canContinue = true
		}

		if src[j] == tgt[j] {
			j--
			canContinue = true
		}

		if !canContinue {
			break
		}
	}

	src, tgt = src[i:j+1], tgt[i:j+1]
	size = j + 1

	if s.DebugMode() {
		fmt.Println(src, tgt)
	}

	store := make([]int, 26)
	for i := 0; i < size; i++ {
		idx := src[i] - byte('a')
		store[idx]++

		idx = tgt[i] - byte('a')
		store[idx]--
	}

	for i := 0; i < size; i++ {
		if store[i] != 0 {
			return false
		}
	}

	if size <= 2 {
		return true
	}

	return true
}
