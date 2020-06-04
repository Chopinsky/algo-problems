package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// RSQProblems ...
type RSQProblems struct {
	set []*RSQ
}

// Solve ...
func (p *RSQProblems) Solve() {
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

// RSQ ...
type RSQ struct {
	data   [][]int
	query  []int
	output int
}

// CreateRSQ ...
func CreateRSQ() s.Problem {
	set := make([]*RSQ, 0, 4)

	data := [][]int{
		{3, 0, 1, 4, 2},
		{5, 6, 3, 2, 1},
		{1, 2, 0, 1, 5},
		{4, 1, 0, 1, 7},
		{1, 0, 3, 0, 5},
	}

	set = append(set, &RSQ{
		data:   data,
		query:  []int{2, 1, 4, 3},
		output: 8,
	})

	set = append(set, &RSQ{
		data:   data,
		query:  []int{1, 1, 2, 2},
		output: 11,
	})

	set = append(set, &RSQ{
		data:   data,
		query:  []int{1, 2, 2, 4},
		output: 12,
	})

	return &RSQProblems{set}
}

func (p *RSQ) solve() int {
	h, w := len(p.data), len(p.data[0])

	sum := make([][]int, h)
	for i := 0; i < h; i++ {
		sum[i] = make([]int, w)
	}

	var a, b, c int

	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if i > 0 && j > 0 {
				a = sum[i-1][j-1]
			} else {
				a = 0
			}

			if i > 0 {
				b = sum[i-1][j]
			} else {
				b = 0
			}

			if j > 0 {
				c = sum[i][j-1]
			} else {
				b = 0
			}

			sum[i][j] = b + c - a + p.data[i][j]
		}
	}

	x0, y0 := p.query[0]-1, p.query[1]-1
	x1, y1 := p.query[2], p.query[3]
	a, b, c = 0, 0, 0

	if x0 >= 0 && y0 >= 0 {
		a = sum[x0][y0]
	}

	if x0 >= 0 {
		b = sum[x0][y1]
	}

	if y0 >= 0 {
		c = sum[x1][y0]
	}

	return sum[x1][y1] - b - c + a
}
