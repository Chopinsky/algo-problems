package p0

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// HIProblems ...
type HIProblems struct {
	set []*HI
}

// Solve ...
func (p *HIProblems) Solve() {
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

// HI ...
type HI struct {
	data   []int
	output int
}

// CreateHI ...
func CreateHI() s.Problem {
	set := make([]*HI, 0, 4)

	set = append(set, &HI{
		data:   []int{},
		output: 0,
	})

	return &HIProblems{set}
}

func (p *HI) solve() int {
	citations := p.data
	size := len(citations)
	if size == 0 {
		return 0
	}

	if size == 1 {
		if citations[0] == 0 {
			return 0
		}

		return 1
	}

	sort.Ints(citations)

	if citations[0] >= size {
		return size
	}

	l, r := 0, size-1
	h := 0

	for l <= r {
		m := (l + r) / 2
		count := size - m

		if citations[m] >= count {
			h = count
			r = m - 1
		} else {
			l = m + 1
		}

		// fmt.Println(m, count, h)
	}

	return h
}
