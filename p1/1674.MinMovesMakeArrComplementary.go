package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MMMACProblems ...
type MMMACProblems struct {
	set []*MMMAC
}

// Solve ...
func (p *MMMACProblems) Solve() {
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

// MMMAC ...
type MMMAC struct {
	data   []int
	limit  int
	output int
}

// CreateMMMAC ...
func CreateMMMAC() s.Problem {
	set := make([]*MMMAC, 0, 4)

	set = append(set, &MMMAC{
		data:   []int{1, 2, 4, 3},
		limit:  4,
		output: 1,
	})

	set = append(set, &MMMAC{
		data:   []int{1, 2, 2, 1},
		limit:  2,
		output: 2,
	})

	set = append(set, &MMMAC{
		data:   []int{1, 2, 1, 2},
		limit:  2,
		output: 0,
	})

	return &MMMACProblems{set}
}

func (p *MMMAC) solve() int {
	size := len(p.data)
	l := p.limit

	// d is the operations taking to get the pair-sum-equals-i for
	// all numbers in the array, so the effective range of d is
	// [2, 2 * limit], where 2 == 1 + 1, and 2*limit = limit+limit
	d := make([]int, 2*l+2)

	for i := 0; i < size/2; i++ {
		a := min(p.data[i], p.data[size-1-i])
		b := max(p.data[i], p.data[size-1-i])

		d[2] += 2  // a dec, b dec
		d[a+1]--   // b dec
		d[a+b]--   // no-op
		d[a+b+1]++ // a inc
		d[l+b+1]++ // a inc, b inc
	}

	ans := -1
	prefix := 0

	// fmt.Println(d)

	for i, val := range d {
		if i <= 1 {
			continue
		}

		prefix += val

		if ans < 0 || prefix < ans {
			ans = prefix
		}
	}

	return ans
}
