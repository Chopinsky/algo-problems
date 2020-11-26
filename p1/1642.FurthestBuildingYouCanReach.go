package p1

import (
	"container/heap"
	"fmt"
	"time"

	s "go-problems/shared"
)

// FBYCRProblems ...
type FBYCRProblems struct {
	set []*FBYCR
}

// Solve ...
func (p *FBYCRProblems) Solve() {
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

// FBYCR ...
type FBYCR struct {
	data   []int
	b      int
	l      int
	output int
}

// CreateFBYCR ...
func CreateFBYCR() s.Problem {
	set := make([]*FBYCR, 0, 4)

	set = append(set, &FBYCR{
		data:   []int{4, 2, 7, 6, 9, 14, 12},
		b:      5,
		l:      1,
		output: 4,
	})

	set = append(set, &FBYCR{
		data:   []int{4, 12, 2, 7, 3, 18, 20, 3, 19},
		b:      10,
		l:      2,
		output: 7,
	})

	set = append(set, &FBYCR{
		data:   []int{14, 3, 19, 3},
		b:      17,
		l:      0,
		output: 3,
	})

	return &FBYCRProblems{set}
}

func (p *FBYCR) solve() int {
	h, b, l := p.data, p.b, p.l
	size := len(h)

	if l >= size {
		return size - 1
	}

	presum := make([]int, size)
	curr := 0

	for i := range h {
		if i == 0 {
			continue
		}

		if h[i] > h[i-1] {
			presum[i] += presum[i-1] + h[i] - h[i-1]
		} else {
			presum[i] = presum[i-1]
		}

		if presum[i] == 0 {
			curr = i
		}
	}

	fmt.Println(presum, b, l, curr)

	if presum[size-1] <= b || curr == size-1 {
		return size - 1
	}

	hp := make(TopQueue, 0, size)

	for curr < size-1 {
		diff := presum[curr+1] - presum[curr]

		if diff > b {
			// no more ladder, or no more places to use the ladder
			if l == 0 {
				break
			}

			fmt.Println(curr, b, l, diff)
			l--

			if hp.Len() == 0 || diff > hp[0] {
				// if no more places for the past, use it here
				curr++
			} else {
				// use a ladder in exchange for some bricks
				b += hp.Pop().(int)
			}

			continue
		}

		if diff > 0 {
			b -= diff
			hp.Push(diff)
		}

		curr++
	}

	return curr
}

// TopQueue ...
type TopQueue []int

// Len ...
func (q TopQueue) Len() int {
	return len(q)
}

// Less ...
func (q TopQueue) Less(i, j int) bool {
	return q[i] > q[j]
}

// Swap ...
func (q TopQueue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}

// Push ...
func (q *TopQueue) Push(val interface{}) {
	v := val.(int)
	*q = append(*q, v)
	heap.Fix(q, q.Len()-1)
}

// Pop ...
func (q *TopQueue) Pop() interface{} {
	old := *q
	n := old.Len()
	pos := old[0]

	old.Swap(0, n-1)
	*q = old[:n-1]

	heap.Fix(q, 0)
	return pos
}
