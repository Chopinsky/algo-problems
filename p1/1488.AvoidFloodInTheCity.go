package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// AFCProblems ...
type AFCProblems struct {
	set []*AFC
}

// Solve ...
func (p *AFCProblems) Solve() {
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

// AFC ...
type AFC struct {
	data   []int
	output []int
}

// CreateAFC ...
func CreateAFC() s.Problem {
	set := make([]*AFC, 0, 4)

	set = append(set, &AFC{
		data:   []int{1, 2, 3, 4},
		output: []int{-1, -1, -1, -1},
	})

	set = append(set, &AFC{
		data:   []int{1, 2, 0, 0, 2, 1},
		output: []int{-1, -1, 2, 1, -1, -1},
	})

	set = append(set, &AFC{
		data:   []int{1, 2, 0, 2, 1},
		output: []int{},
	})

	set = append(set, &AFC{
		data:   []int{69, 0, 0, 0, 69},
		output: []int{-1, 69, 1, 1, -1},
	})

	set = append(set, &AFC{
		data:   []int{10, 20, 20},
		output: []int{},
	})

	return &AFCProblems{set}
}

func (p *AFC) solve() []int {
	size := len(p.data)
	lakes := make(map[int]int)
	days := make([]int, 0, size)
	res := make([]int, size)

	for i, val := range p.data {
		if val > 0 {
			res[i] = -1

			if day, ok := lakes[val]; ok {
				drainDay := findLastDay(days, day)

				// fmt.Println(i, val, days, day, drainDay)

				if drainDay < 0 {
					return []int{}
				}

				res[days[drainDay]] = val
				lakes[val] = i

				copy(days[drainDay:], days[drainDay+1:])
				days = days[:len(days)-1]
			} else {
				lakes[val] = i
			}
		} else {
			days = append(days, i)
		}
	}

	if len(days) > 0 {
		for i := range days {
			res[days[i]] = 1
		}
	}

	return res
}

func findLastDay(days []int, day int) int {
	if len(days) == 0 || day > days[len(days)-1] {
		return -1
	}

	l, r := 0, len(days)-1
	last := -1

	for l <= r {
		m := (l + r) / 2
		if days[m] > day {
			last = m
			r = m - 1
		} else {
			l = m + 1
		}
	}

	return last
}
