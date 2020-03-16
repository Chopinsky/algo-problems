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

	return &SSProblems{set}
}

var a = byte('a')
var m map[string]bool

func (p *SS) solve() bool {
	m = make(map[string]bool)

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

	size = j + 1
	if size <= 3 {
		return true
	}

	src, tgt = src[i:j+1], tgt[i:j+1]

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

	return p.verify(src, tgt, size)
}

func (p *SS) verify(src, tgt string, size int) bool {
	if size <= 3 {
		return true
	}

	var key string
	if src < tgt {
		key = src + "," + tgt
	} else {
		key = tgt + "," + src
	}

	if val, ok := m[key]; ok {
		return val
	}

	sHash, tHash, trHash := 0, 0, 0
	result := false

	for i := 0; i < size-1; i++ {
		sKey, tKey, trKey := int(src[i]-a), int(tgt[i]-a), int(tgt[size-1-i]-a)

		sHash += sKey * 100
		tHash += tKey * 100
		trHash += trKey * 100

		if s.DebugMode() {
			fmt.Println(string(src[i]), string(tgt[i]), string(tgt[size-1-i]))
			fmt.Println(sKey, tKey, trKey, "\n")
		}

		if sHash == tHash {
			if p.verify(src[:i+1], tgt[:i+1], i) && p.verify(src[i+1:], tgt[i+1:], size-i) {
				result = true
				break
			}
		}

		if sHash == trHash {
			if p.verify(src[:i+1], tgt[size-i-1:], i) && p.verify(src[i+1:], tgt[:size-i-1], size-i) {
				result = true
				break
			}
		}
	}

	m[key] = result

	return result
}
