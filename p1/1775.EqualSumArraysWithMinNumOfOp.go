package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// ESAMNOProblems ...
type ESAMNOProblems struct {
	set []*ESAMNO
}

// Solve ...
func (p *ESAMNOProblems) Solve() {
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

// ESAMNO ...
type ESAMNO struct {
	a      []int
	b      []int
	output int
}

// CreateESAMNO ...
func CreateESAMNO() s.Problem {
	set := make([]*ESAMNO, 0, 4)

	set = append(set, &ESAMNO{
		a:      []int{1, 2, 3, 4, 5, 6},
		b:      []int{1, 1, 2, 2, 2, 2},
		output: 3,
	})

	set = append(set, &ESAMNO{
		a:      []int{1, 1, 1, 1, 1, 1, 1},
		b:      []int{6},
		output: -1,
	})

	set = append(set, &ESAMNO{
		a:      []int{6, 6},
		b:      []int{1},
		output: 3,
	})

	return &ESAMNOProblems{set}
}

func (p *ESAMNO) solve() int {
	a, b := p.a, p.b
	la, lb := len(a), len(b)

	if la > 6*lb || 6*la < lb {
		return -1
	}

	var sa, sb int
	for _, val := range a {
		sa += val
	}

	for _, val := range b {
		sb += val
	}

	if sa == sb {
		return 0
	}

	if sa > sb {
		a, b = b, a
		sa, sb = sb, sa
		la, lb = lb, la
	}

	sort.Ints(a)
	sort.Slice(b, func(i, j int) bool { return b[i] > b[j] })

	// fmt.Println(sa, sb, a, b)
	var i, j, d, diff, da, db, ans int

	for sa != sb && (i < la || j < lb) {
		da, db = 0, 0
		diff = sb - sa

		if i < la {
			da = 6 - a[i]
		}

		if j < lb {
			db = b[j] - 1
		}

		// max(da, db) gives the most this op can give, but it's bound
		// to diff, which is the target we need
		d = min(diff, max(da, db))

		// only use the number that can gives the most to reduce the diff
		if da >= db {
			sa += d
			i++
		} else {
			sb -= d
			j++
		}

		// take the op
		ans++
	}

	// fmt.Println("end", sa, sb, ans, i, j)

	// if we can't get to the equal condition, false
	if sa != sb {
		return -1
	}

	return ans
}
