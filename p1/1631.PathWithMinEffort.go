package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// PMEProblems ...
type PMEProblems struct {
	set []*PME
}

// Solve ...
func (p *PMEProblems) Solve() {
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

// PME ...
type PME struct {
	data   [][]int
	output int
}

// CreatePME ...
func CreatePME() s.Problem {
	set := make([]*PME, 0, 4)

	set = append(set, &PME{
		data: [][]int{
			{1, 2, 2}, {3, 8, 2}, {5, 3, 5},
		},
		output: 2,
	})

	set = append(set, &PME{
		data: [][]int{
			{1, 2, 3}, {3, 8, 4}, {5, 3, 5},
		},
		output: 1,
	})

	set = append(set, &PME{
		data: [][]int{
			{1, 2, 1, 1, 1},
			{1, 2, 1, 2, 1},
			{1, 2, 1, 2, 1},
			{1, 2, 1, 2, 1},
			{1, 1, 1, 2, 1},
		},
		output: 0,
	})

	return &PMEProblems{set}
}

func (p *PME) solve() int {
	grid := p.data
	h, w := len(grid), len(grid[0])
	dirs := []int{-1, 0, 1, 0, -1}

	dp := make([][]int, h)
	for i := range dp {
		dp[i] = make([]int, w)
		for j := range dp[i] {
			dp[i][j] = -1
		}
	}

	dp[0][0] = 0

	// improvement: use priority queue instead of the stack,
	// now we only pop out the lowest efforts (i.e. min(dp)),
	// and if we reach the lower-right corner, we're done; it
	// essentially reduces to the Dijkstra algorithm
	stack := make([][]int, 0, h*w)
	stack = append(stack, []int{0, 0})
	var curr []int

	for len(stack) > 0 {
		curr, stack = stack[0], stack[1:]
		x, y := curr[0], curr[1]
		currDiff := dp[x][y]

		for i := 0; i < 4; i++ {
			x0, y0 := x+dirs[i], y+dirs[i+1]

			if x0 < 0 || x0 >= h || y0 < 0 || y0 >= w {
				continue
			}

			d := max(currDiff, getEffort(grid, x, y, x0, y0))

			if dp[x0][y0] < 0 || d < dp[x0][y0] {
				dp[x0][y0] = d
				stack = append(stack, []int{x0, y0})
			}
		}

		// fmt.Println(stack)
	}

	return dp[h-1][w-1]
}

func getEffort(grid [][]int, x, y, x0, y0 int) int {
	diff := grid[x][y] - grid[x0][y0]
	if diff < 0 {
		return -diff
	}

	return diff
}
