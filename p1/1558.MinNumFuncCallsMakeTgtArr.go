package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MNFCMTAProblems ...
type MNFCMTAProblems struct {
	set []*MNFCMTA
}

// Solve ...
func (p *MNFCMTAProblems) Solve() {
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

// MNFCMTA ...
type MNFCMTA struct {
	data   []int
	output int
}

// CreateMNFCMTA ...
func CreateMNFCMTA() s.Problem {
	set := make([]*MNFCMTA, 0, 4)

	set = append(set, &MNFCMTA{
		data:   []int{1, 5},
		output: 5,
	})

	set = append(set, &MNFCMTA{
		data:   []int{2, 2},
		output: 3,
	})

	return &MNFCMTAProblems{set}
}

func (p *MNFCMTA) solve() int {
	c := make(map[int][2]int)
	c[0] = [2]int{0, 0}

	sum, maxMvs := 0, 0

	for i := range p.data {
		a, b := countNum(p.data[i], c)

		// count the number of +1 ops
		sum += b

		// find out the max number of x2 moves -- since
		// it's applied to all numbers, we only cares
		// about the max moves required
		if a > maxMvs {
			maxMvs = a
		}

		// fmt.Println(p.data[i], "-", a, b)
	}

	return sum + maxMvs
}

func countNum(num int, c map[int][2]int) (int, int) {
	if v, ok := c[num]; ok {
		return v[0], v[1]
	}

	a, b := 0, 0

	for num > 0 {
		if num&1 == 1 {
			b++
		}

		a++
		num >>= 1
	}

	c[num] = [2]int{a - 1, b}
	return a - 1, b
}
