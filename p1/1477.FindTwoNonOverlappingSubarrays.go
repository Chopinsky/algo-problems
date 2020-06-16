package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// FNSProblems ...
type FNSProblems struct {
	set []*FNS
}

// Solve ...
func (p *FNSProblems) Solve() {
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

// FNS ...
type FNS struct {
	data   []int
	tgt    int
	output int
}

// CreateFNS ...
func CreateFNS() s.Problem {
	set := make([]*FNS, 0, 4)

	set = append(set, &FNS{
		data:   []int{3, 2, 2, 4, 3},
		tgt:    3,
		output: 2,
	})

	set = append(set, &FNS{
		data:   []int{7, 3, 4, 7},
		tgt:    7,
		output: 2,
	})

	set = append(set, &FNS{
		data:   []int{4, 3, 2, 6, 2, 3, 4},
		tgt:    6,
		output: -1,
	})

	set = append(set, &FNS{
		data:   []int{5, 5, 4, 4, 5},
		tgt:    3,
		output: -1,
	})

	set = append(set, &FNS{
		data:   []int{3, 1, 1, 1, 5, 1, 2, 1},
		tgt:    3,
		output: 3,
	})

	return &FNSProblems{set}
}

func (p *FNS) solve() int {
	size := len(p.data)
	subs := make([][]int, 0, size)

	l, r := 0, 0
	sum := p.data[0]

	for l < size {
		if sum == p.tgt {
			subs = append(subs, []int{l, r})

			// shifting the window
			if l < size {
				sum -= p.data[l]
			}

			l++
			r++

			if r < size {
				sum += p.data[r]
			}

			continue
		}

		if sum < p.tgt {
			if r >= size-1 {
				break
			}

			r++
			sum += p.data[r]

			continue
		}

		if l < size {
			sum -= p.data[l]
		}

		l++
	}

	// fmt.Println(subs)

	count := len(subs)
	if count < 2 {
		return -1
	}

	best, lLen, rLen := -1, 0, 0

	for i := 0; i < count-1; i++ {
		lLen = subs[i][1] - subs[i][0] + 1
		if best != -1 && lLen >= best {
			continue
		}

		for j := count - 1; j > i; j-- {
			if subs[i][1] >= subs[j][0] {
				break
			}

			rLen = subs[j][1] - subs[j][0] + 1
			if best == -1 || lLen+rLen < best {
				best = lLen + rLen
			}
		}
	}

	return best
}
