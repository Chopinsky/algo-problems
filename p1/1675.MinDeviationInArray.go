package p1

import (
	"container/heap"
	"fmt"
	"time"

	s "go-problems/shared"
)

// MDAProblems ...
type MDAProblems struct {
	set []*MDA
}

// Solve ...
func (p *MDAProblems) Solve() {
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

// MDA ...
type MDA struct {
	data   []int
	output int
}

// CreateMDA ...
func CreateMDA() s.Problem {
	set := make([]*MDA, 0, 4)

	set = append(set, &MDA{
		data:   []int{1, 2, 3, 4},
		output: 1,
	})

	set = append(set, &MDA{
		data:   []int{4, 1, 5, 20, 3},
		output: 3,
	})

	set = append(set, &MDA{
		data:   []int{2, 10, 8},
		output: 3,
	})

	return &MDAProblems{set}
}

// idea is that the odd numbers can only be in 2 states: num,
// or 2 * num; while the even numbers can be in multiple states,
// but all these numbers will be smaller, hence: num, num/2, num/4,
// ..., 1. So we begin with multiplying odd numbers by 2, and build
// the priority queue where the top number is the largest, and calculate
// the largest difference between the top number and the smallest one
// (smallest one is pre-determined, or from top/2); since all numbers
// in this sub-array can be divided by 2, we divide the top number
// by 2, and put it back into the queue, until the top number is
// odd, and we can't divide it by 2 anymore.
func (p *MDA) solve() int {
	queue := make(MaxQueue, 0, len(p.data))
	small := -1
	max := -1

	var num, d, top int

	for _, val := range p.data {
		if val%2 == 0 {
			num = val
		} else {
			num = 2 * val
		}

		queue.Push(num)

		if small < 0 || num < small {
			small = num
		}
	}

	// fmt.Println(p.data, small)

	for queue[0]%2 == 0 {
		top = queue.Pop().(int)
		d = abs(top, small)

		if max < 0 || d < max {
			max = d
		}

		queue.Push(top / 2)

		if top/2 < small {
			small = top / 2
		}

		// fmt.Println("running:", queue, small, max)
	}

	d = abs(queue[0], small)
	if max < 0 || d < max {
		max = d
	}

	return max
}

// MaxQueue ...
type MaxQueue []int

// Len ...
func (q MaxQueue) Len() int {
	return len(q)
}

// Less ...
func (q MaxQueue) Less(i, j int) bool {
	return q[i] > q[j]
}

// Swap ...
func (q MaxQueue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}

// Push ...
func (q *MaxQueue) Push(val interface{}) {
	v := val.(int)
	*q = append(*q, v)
	heap.Fix(q, q.Len()-1)
}

// Pop ...
func (q *MaxQueue) Pop() interface{} {
	old := *q
	n := old.Len()
	item := old[0]

	old.Swap(0, n-1)
	*q = old[:n-1]
	heap.Fix(q, 0)

	return item
}

/*
func (p *MDA) solve1() int {
	store := make([]int, 0, len(p.data))
	max := -1

	for _, val := range p.data {
		num := downgrade(val)

		if num > 1 && num%2 == 1 && num > max {
			max = num
		}

		store = append(store, num)
	}

	// fmt.Println(p.data)
	// fmt.Println(store, max)

	maxDiff := -1
	for i, val := range p.data {
		d := diff(max, store[i], val)
		if maxDiff < 0 || d > maxDiff {
			maxDiff = d
		}
	}

	return maxDiff
}

func downgrade(val int) int {
	if val == 1 {
		return 1
	}

	v := val
	for v > 1 && v%2 == 0 {
		v /= 2
	}

	if v == 1 {
		return val
	}

	return v
}

func diff(base, val, src int) int {
	if val == base || src == base {
		return 0
	}

	d := abs(val, base)

	if val%2 == 0 {
		for val >= 1 {
			dv := abs(val, base)
			if dv < d {
				d = dv
			}

			val /= 2
		}
	} else {
		// check numbers from `val` to `src`
		for val <= src {
			dv := abs(val, base)
			if dv < d {
				d = dv
			}

			val *= 2
		}
	}

	// if the original number is odd, it can multiply by 2
	if src%2 == 1 {
		dv := abs(2*src, base)
		if dv < d {
			d = dv
		}
	}

	return d
}
*/

func abs(a, b int) int {
	if a >= b {
		return a - b
	}

	return b - a
}
