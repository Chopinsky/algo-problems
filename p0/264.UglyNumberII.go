package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// UNIIProblems ...
type UNIIProblems struct {
	set []*UNII
}

// Solve ...
func (p *UNIIProblems) Solve() {
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

// UNII ...
type UNII struct {
	data   int
	output int
}

// CreateUNII ...
func CreateUNII() s.Problem {
	set := make([]*UNII, 0, 4)

	set = append(set, &UNII{
		data:   10,
		output: 12,
	})

	return &UNIIProblems{set}
}

func (p *UNII) solve() int {
	return nthUglyNumber(p.data)
}

// 3 pointers moving at different speed: each with underlying number
// to times 2, 3, or 5. Keep shifting the pointers, and if there're
// result collisions, shift all collided pointers.
func nthUglyNumber(n int) int {
	if n <= 0 {
		return 0
	}

	nums := make([]int, n)
	nums[0] = 1

	var i, j, k, a, b, c, val int

	for idx := 1; idx < n; idx++ {
		a, b, c = nums[i]*2, nums[j]*3, nums[k]*5

		val = min(a, b, c)
		nums[idx] = val

		if val == a {
			i++
		}

		if val == b {
			j++
		}

		if val == c {
			k++
		}
	}

	// fmt.Println(nums)

	return nums[n-1]
}

func min(a, b, c int) int {
	m := a

	if m > b {
		m = b
	}

	if m > c {
		m = c
	}

	return m
}
