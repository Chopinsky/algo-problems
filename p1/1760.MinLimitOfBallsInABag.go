package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MLBBProblems ...
type MLBBProblems struct {
	set []*MLBB
}

// Solve ...
func (p *MLBBProblems) Solve() {
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

// MLBB ...
type MLBB struct {
	data   []int
	op     int
	output int
}

// CreateMLBB ...
func CreateMLBB() s.Problem {
	set := make([]*MLBB, 0, 4)

	set = append(set, &MLBB{
		data:   []int{9},
		op:     2,
		output: 3,
	})

	set = append(set, &MLBB{
		data:   []int{2, 4, 8, 2},
		op:     4,
		output: 2,
	})

	set = append(set, &MLBB{
		data:   []int{7, 17},
		op:     2,
		output: 7,
	})

	return &MLBBProblems{set}
}

func (p *MLBB) solve() int {
	d := p.data
	maxNum := d[0]

	for _, val := range d {
		if val > maxNum {
			maxNum = val
		}
	}

	// guess the max number in any bag: must be in the [l, r] rnage,
	// and we try to figure out the total ops to get this result
	l, r := 1, maxNum

	for l < r {
		m := (l + r) / 2

		// calc number of operations to get a number of bags,
		// where the maximum balls in any bag will be m
		ops := 0
		for _, val := range d {
			// no need to divide the bag, we already get the max
			// count under the desired number
			if val <= m {
				continue
			}

			// more balls than m, now divid the bag into a number of
			// bags and make sure the bag with the most balls is still
			// smaller than m
			ops += (val - 1) / m
		}

		// if total ops is smaller or equal to the bounds, we can try
		// a smaller m; otherwise, we must raise the lower bounds because
		// we can't get this result with `p.op` ops
		if ops <= p.op {
			r = m
		} else {
			l = m + 1
		}
	}

	return l
}

func (p *MLBB) solve1() int {
	q := make(IntQueue, 0, len(p.data))
	for _, val := range p.data {
		q.Push(-val)
	}

	op := p.op
	var a, b int

	for op > 0 {
		top := -1 * q.Pop().(int)

		if q.Len() == 0 {
			a = top / (op + 1)
		} else if op == 1 || -q[0]*2 >= top {
			a = top / 2
		} else {
			a = -q[0]
		}

		b = top - a
		q.Push(-a)
		q.Push(-b)

		// fmt.Println(op, top, a, b)

		op--
	}

	return -q[0]
}
