package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// SDVCBProblems ...
type SDVCBProblems struct {
	set []*SDVCB
}

// Solve ...
func (p *SDVCBProblems) Solve() {
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

// SDVCB ...
type SDVCB struct {
	data   []int
	order  int
	output int
}

// CreateSDVCB ...
func CreateSDVCB() s.Problem {
	set := make([]*SDVCB, 0, 4)

	set = append(set, &SDVCB{
		data:   []int{2, 5},
		order:  4,
		output: 14,
	})

	set = append(set, &SDVCB{
		data:   []int{3, 5},
		order:  6,
		output: 19,
	})

	set = append(set, &SDVCB{
		data:   []int{2, 8, 4, 10, 6},
		order:  20,
		output: 110,
	})

	set = append(set, &SDVCB{
		data:   []int{1000000000},
		order:  1000000000,
		output: 21,
	})

	return &SDVCBProblems{set}
}

func (p *SDVCB) solve() int {
	mod := int64(1000000007)
	sum := int64(0)
	inv, order := p.data, p.order

	sort.Ints(inv)

	size := len(inv)
	idx := size - 1
	var step int64

	for order > 0 {
		count := int64(size - idx)

		if idx > 0 {
			step = int64(inv[idx] - inv[idx-1])
		} else {
			step = int64(inv[idx])
		}

		// fmt.Println(order, count, idx, val)

		if int(count*step) > order {
			step = int64(order) / count

			if step > 0 {
				sum += (int64(2*inv[idx]-int(step)+1) * step / 2) * count
			}

			count = int64(order) - step*count
			sum += (int64(inv[idx]) - step) * count
			sum %= mod

			break
		}

		if idx > 0 {
			sum += ((int64(inv[idx]+inv[idx-1]+1) % mod) * step / 2) * count
		} else {
			sum += ((int64(1+inv[0]) * step) % mod) / 2 * count
		}

		sum %= mod
		order -= int(count * step)

		if idx > 0 {
			idx--
		}
	}

	return int(sum % mod)
}
