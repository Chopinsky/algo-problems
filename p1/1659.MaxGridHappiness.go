package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MGHProblems ...
type MGHProblems struct {
	set []*MGH
}

// Solve ...
func (p *MGHProblems) Solve() {
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

// MGH ...
type MGH struct {
	m      int
	n      int
	ic     int
	ec     int
	output int
}

// CreateMGH ...
func CreateMGH() s.Problem {
	set := make([]*MGH, 0, 4)

	set = append(set, &MGH{
		m:      2,
		n:      3,
		ic:     1,
		ec:     2,
		output: 240,
	})

	set = append(set, &MGH{
		m:      3,
		n:      1,
		ic:     2,
		ec:     1,
		output: 260,
	})

	set = append(set, &MGH{
		m:      2,
		n:      2,
		ic:     4,
		ec:     0,
		output: 240,
	})

	set = append(set, &MGH{
		m:      5,
		n:      5,
		ic:     6,
		ec:     6,
		output: 1090,
	})

	return &MGHProblems{set}
}

func (p *MGH) solve() int {
	m, n := p.m, p.n
	if m > n {
		m, n = n, m
	}

	grid := make([][]int, m)
	for i := range grid {
		grid[i] = make([]int, n)
	}

	var oi, oe, maxScore int
	cache := make(map[string]int)

	for i := 0; i < 3; i++ {
		grid[0][0] = i
		base := 0

		if i == 1 {
			oi = -1
			oe = 0
			base = 120
		} else if i == 2 {
			oi = 0
			oe = -1
			base = 40
		}

		score := addPerson(grid, cache, i, 0, 1, m, n, p.ic+oi, p.ec+oe, base)
		if score > maxScore {
			maxScore = score
		}
	}

	return maxScore
}

func addPerson(grid [][]int, cache map[string]int, gridKey, i, j, h, w, ic, ec, score int) int {
	// illegal case
	if ic < 0 || ec < 0 {
		return 0
	}

	// end game case
	if (ic == 0 && ec == 0) || (i == h-1 && j >= w) {
		return score
	}

	var oi, oe, nextMax int
	var up, left, count int

	if j >= w {
		i++
		j = 0
	}

	key := fmt.Sprint(gridKey, i*w+j, ic, ec)
	if val, ok := cache[key]; ok {
		return val
	}

	base := []int{0, 120, 40}
	extra := []int{0, -30, 20}

	if i > 0 {
		up = grid[i-1][j]
	} else {
		up = 0
	}

	if j > 0 {
		left = grid[i][j-1]
	} else {
		left = 0
	}

	if up > 0 {
		count++
	}

	if left > 0 {
		count++
	}

	mask := 1<<(2*w+1) - 1

	for k := 0; k < 3; k++ {
		grid[i][j] = k
		gain := base[k] + count*extra[k]

		if k > 0 {
			if k == 1 {
				oi = -1
				oe = 0
			} else {
				oi = 0
				oe = -1
			}

			gain += extra[up] + extra[left]
		}

		currKey := ((gridKey << 2) & mask) | k
		nextScore := addPerson(grid, cache, currKey, i, j+1, h, w, ic+oi, ec+oe, score+gain)

		if nextScore > nextMax {
			nextMax = nextScore
		}
	}

	// fmt.Println(i, j, ic, ec, nextMax)

	cache[key] = nextMax
	return nextMax
}
