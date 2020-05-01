package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// DTIIProblems ...
type DTIIProblems struct {
	set []*DTII
}

// Solve ...
func (p *DTIIProblems) Solve() {
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

	fmt.Println("Algorithm took", time.Since(start))
}

// DTII ...
type DTII struct {
	data   [][]int
	output []int
}

// CreateDTII ...
func CreateDTII() s.Problem {
	set := make([]*DTII, 0, 4)

	set = append(set, &DTII{
		data:   [][]int{
			{1, 2, 3},
			{4, 5, 6},
			{7, 8, 9},
		},
		output: []int{ 1, 4, 2, 7, 5, 3, 8, 6, 9 },
	})

	set = append(set, &DTII{
		data:   [][]int{
			{1, 2, 3, 4, 5},
			{6, 7},
			{8},
			{9, 10, 11},
			{12, 13, 14, 15, 16},
		},
		output: []int{1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16},
	})

	set = append(set, &DTII{
		data:   [][]int{
			{1, 2, 3},
			{4}, 
			{5, 6, 7},
			{8}, 
			{9, 10, 11},
		},
		output: []int{1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11},
	})	

	set = append(set, &DTII{
		data:   [][]int{
			{1, 2, 3, 4, 5, 6},
		},
		output: []int{1, 2, 3, 4, 5, 6},
	})

	return &DTIIProblems{set}
}

func (p *DTII) solve() []int {
	h := len(p.data)
	if h == 1 {
		return p.data[0]
	}

	list := make(map[int][]int, h)
	top, count := 0, 0

	for i := 0; i < h; i++ {
		w := len(p.data[i])
		for j := 0; j < w; j++ {
			list[i+j] = append(list[i+j], p.data[i][j])
			count++

			if i+j > top {
				top = i + j
			}
		}
	}

	result := make([]int, 0, count)
	for i := 0; i <= top; i++ {
		if arr, ok := list[i]; ok {
			size := len(arr)
			for i := size - 1; i >= 0; i-- {
				result = append(result, arr[i])
			}
		}
	}	

	return result
}
