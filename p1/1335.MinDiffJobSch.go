package p1

import (
	s "go-problems/shared"
	"strconv"
)

// MDJSProblems ...
type MDJSProblems struct {
	set []*MDJS
}

// Solve ...
func (p *MDJSProblems) Solve() {
	for i, p := range p.set {
		result := p.solve()

		s.Print(i, strconv.Itoa(p.output), strconv.Itoa(result))
	}
}

// CreateMDJS ...
func CreateMDJS() s.Problem {
	set := make([]*MDJS, 0, 4)

	set = append(set, &MDJS{
		data:   []int{6, 5, 4, 3, 2, 1},
		day:    2,
		output: 7,
	})

	set = append(set, &MDJS{
		data:   []int{9, 9, 9},
		day:    4,
		output: -1,
	})

	set = append(set, &MDJS{
		data:   []int{1, 1, 1},
		day:    3,
		output: 3,
	})

	set = append(set, &MDJS{
		data:   []int{7, 1, 7, 1, 7, 1},
		day:    3,
		output: 15,
	})

	set = append(set, &MDJS{
		data:   []int{11, 111, 22, 222, 33, 333, 44, 444},
		day:    6,
		output: 843,
	})

	return &MDJSProblems{set}
}

// MDJS ...
type MDJS struct {
	data   []int
	day    int
	output int
}

var max = 1<<16 - 1

func (p *MDJS) solve() int {
	size, day := len(p.data), p.day

	if size < p.day {
		return -1
	}

	if size == p.day {
		sum := 0
		for i := 0; i < size; i++ {
			sum += p.data[i]
		}

		return sum
	}

	dp := make([][]int, size+1)
	for i := 0; i < size+1; i++ {
		dp[i] = make([]int, day+1)
		for j := 0; j < day+1; j++ {
			dp[i][j] = max
		}
	}

	dp[0][0] = 0

	return 0
}
