package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// SGIIIProblems ...
type SGIIIProblems struct {
	set []*SGIII
}

// Solve ...
func (p *SGIIIProblems) Solve() {
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

// SGIII ...
type SGIII struct {
	data   []int
	output string
}

// CreateSGIII ...
func CreateSGIII() s.Problem {
	set := make([]*SGIII, 0, 6)

	set = append(set, &SGIII{
		data:   []int{1, 2, 3, 7},
		output: "bob",
	})

	set = append(set, &SGIII{
		data:   []int{1, 2, 3, -9},
		output: "alice",
	})

	set = append(set, &SGIII{
		data:   []int{1, 2, 3, 6},
		output: "tie",
	})

	set = append(set, &SGIII{
		data:   []int{1, 2, 3, -1, -2, -3, 7},
		output: "alice",
	})

	set = append(set, &SGIII{
		data:   []int{-1, -2, -3},
		output: "tie",
	})

	return &SGIIIProblems{set}
}

func (p *SGIII) solve() string {
	// alice -- player 1;
	// bob   -- player -1;
	b0, b1 := p.play(0, 1, 0, 0, len(p.data))

	if b0 > b1 {
		return "alice"
	} else if b0 < b1 {
		return "bob"
	} else {
		return "tie"
	}
}

func (p *SGIII) play(start, player, p0, p1, size int) (int, int) {
	if start >= size {
		return p0, p1
	}

	if size-start <= 3 {
		acc, valid := 0, true

		for i := start; i < size; i++ {
			// if a negative number exists, the game plan gets complicated,
			// and we can't optimize this situation right here.
			if p.data[i] < 0 {
				valid = false
				break
			}

			acc += p.data[i]
		}

		if valid {
			if player == 1 {
				return p0 + acc, p1
			}

			return p0, p1 + acc
		}
	}

	var g0, g1, b0, b1 int
	var pos int

	for i := start; i < start+3; i++ {
		if i >= size {
			break
		}

		if player == 1 {
			p0 += p.data[i]
		} else {
			p1 += p.data[i]
		}

		g0, g1 = p.play(i+1, -1*player, p0, p1, size)

		if i == start || (g0-g1)*player > (b0-b1)*player {
			pos = i
			b0, b1 = g0, g1
		}
	}

	if s.DebugMode() && start == 0 {
		fmt.Println(start, player, b0, b1, pos)
	}

	return b0, b1
}
