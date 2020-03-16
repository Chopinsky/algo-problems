package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MCMLPProblems ...
type MCMLPProblems struct {
	set []*MCMLP
}

// Solve ...
func (p *MCMLPProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= count; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == count {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm took", time.Since(start))
}

// MCMLP ...
type MCMLP struct {
	data   [][]int
	output int
}

// CreateMCMLP ...
func CreateMCMLP() s.Problem {
	set := make([]*MCMLP, 0, 4)

	set = append(set, &MCMLP{
		data: [][]int{
			{1, 1, 1, 1},
			{2, 2, 2, 2},
			{1, 1, 1, 1},
			{2, 2, 2, 2},
		},
		output: 3,
	})

	set = append(set, &MCMLP{
		data: [][]int{
			{1, 1, 3},
			{3, 2, 2},
			{1, 1, 4},
		},
		output: 0,
	})

	return &MCMLPProblems{set}
}

func (p *MCMLP) solve() int {
	stack := []*state{&state{
		pos:      [2]int{0, 0},
		cost:     0,
		visited:  0,
		modifies: 0,
	}}

	h, w := len(p.data), len(p.data[0])

	scores := make([][]int, h)
	for i := 0; i < h; i++ {
		scores[i] = make([]int, w)
		for j := 0; j < w; j++ {
			scores[i][j] = 1 << 16
		}
	}

	best := 1 << 16
	var next *state

	for len(stack) > 0 {
		next, stack = stack[0], stack[1:]
		scores, stack, best = next.move(scores, p.data, stack, best, h, w)
	}

	if s.DebugMode() {
		fmt.Println(scores)
	}

	return best
}

type state struct {
	pos      [2]int
	cost     int
	visited  int
	modifies int
}

func (st *state) move(scores, grid [][]int, stack []*state, best, h, w int) ([][]int, []*state, int) {
	if st.cost >= best {
		return scores, stack, best
	}

	x, y := st.pos[0], st.pos[1]
	dir := grid[x][y]
	visited := st.visited | (1 << uint(x*w+y))
	modifies := st.modifies | (1 << uint(x*w+y))

	// fmt.Println(x, y, dir, visited, modifies)

	var nextCost int

	for i := 0; i < 4; i++ {
		x0, y0 := x+s.Dirs[i], y+s.Dirs[i+1]

		if x0 >= 0 && x0 < h && y0 >= 0 && y0 < w {
			if (i == 0 && dir == 4) || (i == 1 && dir == 1) || (i == 2 && dir == 3) || (i == 3 && dir == 2) {
				// we can go to this slot
				nextCost = st.cost
			} else if modifies != st.modifies {
				// we can modify the current slot to go to this slot
				nextCost = st.cost + 1
			} else {
				// there's no way to reach this slot
				continue
			}

			if nextCost >= best {
				continue
			}

			if (visited&(1<<uint(x0*w+y0)) == 0) || (nextCost < scores[x0][y0]) {
				// not yet visited, or we can get here with better scores, add it to the stack
				scores[x0][y0] = nextCost

				if x0 == h-1 && y0 == w-1 {
					best = nextCost
					continue
				}

				if nextCost != st.cost {
					stack = append(stack, &state{
						pos:      [2]int{x0, y0},
						cost:     nextCost,
						visited:  visited,
						modifies: modifies,
					})
				} else {
					stack = append(stack, &state{
						pos:      [2]int{x0, y0},
						cost:     nextCost,
						visited:  visited,
						modifies: st.modifies,
					})
				}
			}
		}
	}

	return scores, stack, best
}
