package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// CPIIProblems ...
type CPIIProblems struct {
	set []*CPII
}

// Solve ...
func (p *CPIIProblems) Solve() {
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

// CPII ...
type CPII struct {
	data   [][]int
	output int
}

// CreateCPII ...
func CreateCPII() s.Problem {
	set := make([]*CPII, 0, 4)

	set = append(set, &CPII{
		data: [][]int{
			{3, 1, 1},
			{2, 5, 1},
			{1, 5, 5},
			{2, 1, 1},
		},
		output: 24,
	})

	set = append(set, &CPII{
		data: [][]int{
			{1, 0, 0, 0, 0, 0, 1},
			{2, 0, 0, 0, 0, 3, 0},
			{2, 0, 9, 0, 0, 0, 0},
			{0, 3, 0, 5, 4, 0, 0},
			{1, 0, 2, 3, 0, 0, 6},
		},
		output: 28,
	})

	set = append(set, &CPII{
		data: [][]int{
			{1, 0, 0, 3},
			{0, 0, 0, 3},
			{0, 0, 3, 3},
			{9, 0, 3, 3},
		},
		output: 22,
	})

	set = append(set, &CPII{
		data: [][]int{
			{1, 1},
			{1, 1},
		},
		output: 4,
	})

	return &CPIIProblems{set}
}

var dirs2 = []int{-1, -1, 0, 0, 1, 1, 0, -1, 1, -1}

func (p *CPII) solve() int {
	h, w, grid := len(p.data), len(p.data[0]), p.data
	dp := make([][][]int, w)

	for i := 0; i < w; i++ {
		dp[i] = make([][]int, w)
		for j := 0; j < w; j++ {
			dp[i][j] = make([]int, 2)
		}

		if i == 0 {
			dp[0][w-1][0] = grid[0][0] + grid[0][w-1]
		}
	}

	last, curr, r := 0, 1, 1
	var val, max int

	for r < h {
		for i := 0; i < w; i++ {
			for j := 0; j < w; j++ {
				// reset the value
				dp[i][j][curr] = 0

				for k := 0; k < 9; k++ {
					a, b := i+dirs2[k], j+dirs2[k+1]
					if a < 0 || b < 0 || a >= w || b >= w {
						continue
					}

					if i == j {
						val = dp[a][b][last] + grid[r][i]
					} else {
						val = dp[a][b][last] + grid[r][i] + grid[r][j]
					}

					if val > dp[i][j][curr] {
						dp[i][j][curr] = val
					}
				}

				if r == h-1 && dp[i][j][curr] > max {
					max = dp[i][j][curr]
				}
			}
		}

		last, curr = curr, last
		r++
	}

	return max
}

func (p *CPII) solve1() int {
	h, w, grid := len(p.data), len(p.data[0]), p.data

	row := map[int]int{
		w - 1: grid[0][0] + grid[0][w-1],
	}

	r := 1
	c := 0

	for r < h {
		currRow := make(map[int]int)

		for k, v := range row {
			a, b := getKeys(k, w)

			for i := -1; i <= 1; i++ {
				for j := -1; j <= 1; j++ {
					na, nb := a+i, b+j

					// invalid positions
					if na < 0 || nb < 0 || na >= w || nb >= w {
						continue
					}

					// a valid position
					if na == nb {
						c = v + grid[r][na]
					} else {
						c = v + grid[r][na] + grid[r][nb]
					}

					key := setKey(na, nb, w)
					if c > currRow[key] {
						currRow[key] = c
					}
				}
			}
		}

		row = currRow
		r++
	}

	max := 0
	for _, v := range row {
		if v > max {
			max = v
		}
	}

	return max
}

func setKey(i, j, pad int) int {
	return i*pad + j
}

func getKeys(key, pad int) (int, int) {
	return key / pad, key % pad
}
