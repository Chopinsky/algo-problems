package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// RSSSProblems ...
type RSSSProblems struct {
	set []*RSSS
}

// Solve ...
func (p *RSSSProblems) Solve() {
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

// RSSS ...
type RSSS struct {
	data   []int
	n      int
	l      int
	r      int
	output int
}

// CreateRSSS ...
func CreateRSSS() s.Problem {
	set := make([]*RSSS, 0, 4)

	set = append(set, &RSSS{
		data:   []int{1, 2, 3, 4},
		n:      4,
		l:      1,
		r:      5,
		output: 13,
	})

	set = append(set, &RSSS{
		data:   []int{1, 2, 3, 4},
		n:      4,
		l:      3,
		r:      4,
		output: 6,
	})

	set = append(set, &RSSS{
		data:   []int{1, 2, 3, 4},
		n:      4,
		l:      1,
		r:      10,
		output: 50,
	})

	return &RSSSProblems{set}
}

// use min-heap
func (p *RSSS) solve() int {
	h := s.IntHeapInit(p.data)

	l, r := p.l, p.r
	size := len(p.data)
	presum := make([]int, r+1)

	for i := 0; i < r; i++ {
		top := h.Pop().([]int)
		presum[i+1] = presum[i] + top[0]

		top[1]++
		if top[1] < size {
			top[0] += p.data[top[1]]
			h.Push(top)
		}
	}

	fmt.Println(presum)

	return presum[r]-presum[l-1]
}

func (p *RSSS) solve1() int {
	size := len(p.data)
	l, r := p.l, p.r

	presum := make([]int, size+1)
	for i := range p.data {
		presum[i+1] = presum[i] + p.data[i]
	}

	sums := make([]int, 0, size*(size+1)/2)
	for i := range p.data {
		for j := i; j < size; j++ {
			sums = append(sums, presum[j+1]-presum[i])
		}
	}

	sort.Ints(sums)
	// fmt.Println(presum, sums)

	res := 0
	for i := l - 1; i < r; i++ {
		res += sums[i]
	}

	return res
}
