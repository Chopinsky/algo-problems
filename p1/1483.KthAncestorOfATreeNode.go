package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// KATProblems ...
type KATProblems struct {
	set []*KAT
}

// Solve ...
func (p *KATProblems) Solve() {
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

// KAT ...
type KAT struct {
	data   []int
	query  [][]int
	count  int
	output []int
}

// CreateKAT ...
func CreateKAT() s.Problem {
	set := make([]*KAT, 0, 4)

	set = append(set, &KAT{
		data:   []int{-1, 0, 0, 1, 1, 2, 2, 3, 3},
		query:  [][]int{{3, 1}, {5, 2}, {6, 3}},
		output: []int{1, 0, -1},
	})

	return &KATProblems{set}
}

func (p *KAT) solve() []int {
	res := make([]int, len(p.query))
	store := make([][]int, p.count)

	var k, kp int

	for i, parent := range p.data {
		k, kp = 1, parent
		s := make([]int, 0, i)
		s = append(s, parent)

		for kp != -1 {
			kp = query(store, kp, k, false)
			s = append(s, kp)
			k <<= 1
		}

		store = append(store, s)
	}

	// fmt.Println(store)

	for i, q := range p.query {
		res[i] = query(store, q[0], q[1], false)
	}

	return res
}

func query(src [][]int, p, k int, debug bool) int {
	if p < 0 || k > p {
		return -1
	}

	arr, size := src[p], len(src[p])
	idx := topBitCnt(k)

	if debug {
		fmt.Println(p, k, idx)
	}

	if size < idx {
		return -1
	}

	// kth parent is in the store
	if k == (k & -k) {
		return arr[idx-1]
	}

	// recursively finding the remainder
	return query(src, arr[idx-1], k-(1<<(idx-1)), debug)
}

func topBitCnt(n int) int {
	if n == 0 {
		return 0
	}

	msb := 0
	for n > 0 {
		n >>= 1
		msb++
	}

	return msb
}
