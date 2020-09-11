package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// DESProblems ...
type DESProblems struct {
	set []*DES
}

// Solve ...
func (p *DESProblems) Solve() {
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

// DES ...
type DES struct {
	data   []int
	output int
}

// CreateDES ...
func CreateDES() s.Problem {
	set := make([]*DES, 0, 4)

	set = append(set, &DES{
		data:   []int{},
		output: 0,
	})

	return &DESProblems{set}
}

func (p *DES) solve() int {
	return 0
}

var base = 26

func distinctEchoSubstrings(text string) int {
	size := len(text)

	if size == 1 {
		return 0
	}

	if size == 2 {
		if text[0] == text[1] {
			return 1
		}

		return 0
	}

	count := 0
	sub := make(map[string]bool)
	store := make([]int, size)

	// substring len == 1
	for i := 0; i < size-1; i++ {
		if text[i] == text[i+1] && !sub[text[i:i+1]] {
			count++
			sub[text[i:i+1]] = true
		}
	}

	// substring len: [2, n/2]
	for i := 2; i <= size/2; i++ {
		h := initHash(text, 0, i-1)
		top := calcTop(i)
		store[0] = h

		// fmt.Println("length:", i, h)

		for j := 1; j+i-1 < size; j++ {
			h = rollingHash(h, top*int(text[j-1]), int(text[j+i-1]))
			store[j] = h

			// fmt.Println("pos:", j, h, text[j:j+i])

			if j-i >= 0 && store[j-i] == h && !sub[text[j:j+i]] && text[j-i:j] == text[j:j+i] {
				count++
				sub[text[j:j+i]] = true
			}
		}
	}

	fmt.Println(sub)

	return count
}

func initHash(s string, i, j int) int {
	h := 0

	for k := i; k <= j; k++ {
		h = (h*base)%mod + int(s[k])
	}

	return h % mod
}

func rollingHash(src, top, next int) int {
	return (((src+mod-top)*base)%mod + next) % mod
}

func calcTop(size int) int {
	val := 1

	for i := 0; i < size-1; i++ {
		val = (val * base) % mod
	}

	return val % mod
}

func distinctEchoSubstrings1(text string) int {
	const (
		base = 26
		mod  = 71111113
	)

	size := len(text)
	set := make(map[int64]struct{})
	hash := make([]int64, size+1)

	pow := make([]int64, size+1)
	pow[0] = 1

	for i := 1; i <= size; i++ {
		// 'a' --> 1, ..., 'z' --> 26
		char := int64(text[i-1] - 'a' + 1)

		hash[i] = (hash[i-1]*base + char) % mod
		pow[i] = pow[i-1] * base % mod
	}

	for l := 2; l <= size; l += 2 {
		for i := 0; i+l <= size; i++ {
			mid := i + l/2

			leftHalfHash := getHash(i, mid, mod, hash, pow)
			rightHalfHash := getHash(mid, i+l, mod, hash, pow)

			if leftHalfHash == rightHalfHash {
				set[rightHalfHash] = struct{}{}
			}
		}
	}

	return len(set)
}

func getHash(l, r int, mod int64, hash, pow []int64) int64 {
	return (hash[r] - hash[l]*pow[r-l]%mod + mod) % mod
}
