package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// FCEMSTProblems ...
type FCEMSTProblems struct {
	set []*FCEMST
}

// Solve ...
func (p *FCEMSTProblems) Solve() {
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

// FCEMST ...
type FCEMST struct {
	data   [][]int
	num    int
	output [][]int
}

// CreateFCEMST ...
func CreateFCEMST() s.Problem {
	set := make([]*FCEMST, 0, 4)

	set = append(set, &FCEMST{
		data: [][]int{
			{0, 1, 1},
			{1, 2, 1},
			{2, 3, 2},
			{0, 3, 2},
			{0, 4, 3},
			{3, 4, 3},
			{1, 4, 6},
		},
		num: 5,
		output: [][]int{
			{0, 1},
			{2, 3, 4, 5},
		},
	})

	set = append(set, &FCEMST{
		data: [][]int{
			{0, 1, 1},
			{1, 2, 1},
			{2, 3, 1},
			{0, 3, 1},
		},
		num: 4,
		output: [][]int{
			{},
			{0, 1, 2, 3},
		},
	})

	return &FCEMSTProblems{set}
}

func (p *FCEMST) solve() [][]int {
	size := len(p.data)
	count, edges := s.BuildMST(p.data, p.num)
	total := 1

	store := make(map[int]int)
	for i := range edges {
		store[edges[i][0]]++
	}

	for i := 0; i < size; i++ {
		val := p.data[i][2]
		p.data[i][2] = -1

		c, e := s.BuildMST(p.data, p.num)
		p.data[i][2] = val

		// fmt.Println(i, c)
		if c == -1 || c > count {
			continue
		}

		total++
		for i := range e {
			store[e[i][0]]++
		}
	}

	// fmt.Println(store, total)
	res := make([][]int, 2)

	for k, v := range store {
		if v == total {
			// this is a critical path
			res[0] = append(res[0], k)
		} else {
			// this is a psudo-critical path
			res[1] = append(res[1], k)
		}
	}

	return res
}
