package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// NOIIIProblems ...
type NOIIIProblems struct {
	set []*NOIII
}

// Solve ...
func (p *NOIIIProblems) Solve() {
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

// NOIII ...
type NOIII struct {
	data   [][]int
	m      int
	n      int
	output []int
}

// CreateNOIII ...
func CreateNOIII() s.Problem {
	set := make([]*NOIII, 0, 4)

	set = append(set, &NOIII{
		data:   [][]int{{0, 0}, {0, 1}, {1, 2}, {2, 1}, {1, 1}},
		m:      3,
		n:      3,
		output: []int{1, 1, 2, 3, 1},
	})

	return &NOIIIProblems{set}
}

func (p *NOIII) solve() []int {
	h, w := p.m, p.n
	islands := []int{0}
	ans := make([]int, 0, len(p.data))
	sur := make([]int, 0, 4)
	marks := make([][]int, h)

	for i := range marks {
		marks[i] = make([]int, w)
	}

	var count int
	for _, loc := range p.data {
		x, y := loc[0], loc[1]

		for i := 0; i < 4; i++ {
			x0, y0 := x+dirs[i], y+dirs[i+1]

			if x0 < 0 || x0 >= h || y0 < 0 || y0 >= w || marks[x0][y0] == 0 {
				continue
			}

			sur = append(sur, marks[x0][y0])
		}

		if len(sur) == 1 {
			marks[x][y] = sur[0]
		} else if len(sur) > 1 {
			realID := findi(islands, sur[0])

			for i := 1; i < len(sur); i++ {
				currID := findi(islands, sur[i])

				// fmt.Println(realID, currID)

				if currID != realID {
					count--
				}

				realID = ui(islands, realID, sur[i])
			}

			marks[x][y] = realID
		} else {
			// an isolated, lone island, create an id for it
			id := len(islands)
			islands = append(islands, id)
			marks[x][y] = id
			count++
		}

		// clear and reuse the slice
		sur = sur[:0]

		ans = append(ans, count)
	}

	fmt.Println(marks)

	return ans
}

func ui(u []int, a, b int) int {
	if a == b {
		return a
	}

	sa, sb := findi(u, a), findi(u, b)

	if sa >= sb {
		u[sa] = sb
		return sb
	}

	u[sb] = sa
	return sa
}

func findi(u []int, a int) int {
	for u[a] != a {
		a = u[a]
	}

	return a
}
