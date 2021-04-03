package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// LSWRProblems ...
type LSWRProblems struct {
	set []*LSWR
}

// Solve ...
func (p *LSWRProblems) Solve() {
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

// LSWR ...
type LSWR struct {
	data   [][]int
	output int
}

// CreateLSWR ...
func CreateLSWR() s.Problem {
	set := make([]*LSWR, 0, 4)

	set = append(set, &LSWR{
		data: [][]int{
			{0, 0, 1},
			{1, 1, 1},
			{1, 0, 1},
		},
		output: 4,
	})

	set = append(set, &LSWR{
		data: [][]int{
			{1, 0, 1, 0, 1},
		},
		output: 3,
	})

	set = append(set, &LSWR{
		data: [][]int{
			{1, 1, 0},
			{1, 0, 1},
		},
		output: 2,
	})

	set = append(set, &LSWR{
		data: [][]int{
			{0, 0},
			{0, 0},
		},
		output: 0,
	})

	return &LSWRProblems{set}
}

func (p *LSWR) solve() int {
	matrix := p.data
	h, w := len(matrix), len(matrix[0])
	dp := make([][]int, h)

	for i := range dp {
		dp[i] = make([]int, w)
	}

	for j := 0; j < w; j++ {
		for i := 0; i < h; i++ {
			if matrix[i][j] == 0 {
				continue
			}

			if i == 0 {
				dp[i][j] = 1
			} else {
				dp[i][j] += dp[i-1][j] + 1
			}
		}
	}

	// fmt.Println(dp)

	var count int
	for i := range dp {
		sort.Slice(dp[i], func(ii, jj int) bool {
			return dp[i][ii] > dp[i][jj]
		})

		// fmt.Println(dp[i])

		for j := range dp[i] {
			area := dp[i][j] * (j + 1)
			if area > count {
				count = area
			}
		}
	}

	return count
}
