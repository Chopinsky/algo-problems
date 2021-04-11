package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// PPIVProblems ...
type PPIVProblems struct {
	set []*PPIV
}

// Solve ...
func (p *PPIVProblems) Solve() {
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

// PPIV ...
type PPIV struct {
	data   string
	output bool
}

// CreatePPIV ...
func CreatePPIV() s.Problem {
	set := make([]*PPIV, 0, 4)

	set = append(set, &PPIV{
		data:   "abcbdd",
		output: true,
	})

	set = append(set, &PPIV{
		data:   "bcbddxy",
		output: false,
	})

	return &PPIVProblems{set}
}

func (p *PPIV) solve() bool {
	size := len(p.data)
	dp := make([][2]int, size)

	for i := range p.data {
		dp[i] = [2]int{0, 0}
		dp[i][0], dp[i][1] = findBounds(p.data, i, size)
	}

	// fmt.Println(p.data, "\n", dp)
	var left, right bool
	var idx int

	for i := 1; i < size-1; i++ {
		left, right = false, false

		// i as center, i.e. odd length
		// left - [0, i-j-1]
		// right - [i+j+1, size-1]
		for j := 0; j < dp[i][0]; j++ {
			// overflowed, stop
			if i == j || i+j == size-1 {
				break
			}

			if (i-j)%2 == 0 {
				idx = (i-j)/2 - 1
				if dp[idx][1] >= idx+1 {
					left = true
				}
			} else {
				idx = (i - j - 1) / 2
				if dp[idx][0] >= idx+1 {
					left = true
				}
			}

			if (size-i-j-1)%2 == 0 {
				idx = i + j + (size-i-j-1)/2
				if dp[idx][1] >= idx-i-j {
					right = true
				}
			} else {
				idx = i + j + 1 + (size-i-j-1)/2
				if dp[idx][0] >= idx-i-j {
					right = true
				}
			}

			if left && right {
				return true
			}
		}

		left, right = false, false

		// i and i+1 as center, i.e. even length
		// left - [0, i-j-1]
		// right - [i+j+2, size-1]
		for j := 0; j < dp[i][1]; j++ {
			// overflowed, stop
			if i == j || i+j+1 == size-1 {
				break
			}

			if (i-j)%2 == 0 {
				idx = (i-j)/2 - 1
				if dp[idx][1] >= idx+1 {
					left = true
				}
			} else {
				idx = (i - j - 1) / 2
				if dp[idx][0] >= idx+1 {
					left = true
				}
			}

			if (size-i-j)%2 == 0 {
				idx = i + j + 1 + (size-i-j)/2
				if dp[idx][1] >= idx-i-j-1 {
					right = true
				}
			} else {
				idx = i + j + 2 + (size-i-j)/2
				if dp[idx][0] >= idx-i-j-1 {
					right = true
				}
			}

			if left && right {
				return true
			}
		}
	}

	return false
}

func findBounds(src string, idx, size int) (int, int) {
	var odd, even int
	l, r := idx, idx

	for l >= 0 && r < size && src[l] == src[r] {
		l--
		r++
		odd++
	}

	l, r = idx, idx+1
	for l >= 0 && r < size && src[l] == src[r] {
		l--
		r++
		even++
	}

	return odd, even
}
