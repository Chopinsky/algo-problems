package p1

import (
	"fmt"
	"math/rand"
	"time"

	s "go-problems/shared"
)

// CNTProblems ...
type CNTProblems struct {
	set []*CNT
}

// Solve ...
func (p *CNTProblems) Solve() {
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

// CNT ...
type CNT struct {
	data   []int
	output int
}

// CreateCNT ...
func CreateCNT() s.Problem {
	set := make([]*CNT, 0, 4)

	set = append(set, &CNT{
		data:   []int{2, 5, 3, 4, 1},
		output: 3,
	})

	set = append(set, &CNT{
		data:   []int{2, 1, 3},
		output: 0,
	})

	set = append(set, &CNT{
		data:   []int{1, 2, 3, 4},
		output: 4,
	})

	sudo := make([]int, 200)
	sudo[0] = 1

	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)

	for i := 1; i < 200; i++ {
		sudo[i] = i + 1

		pos := r1.Intn(i)
		if pos == i {
			continue
		}

		sudo[i], sudo[pos] = sudo[pos], sudo[i]
	}

	set = append(set, &CNT{
		data:   sudo,
		output: 0,
	})

	return &CNTProblems{set}
}

func (p *CNT) solve() int {
	size := len(p.data)
	larger, smaller := make([]int, size), make([]int, size)

	for i := 0; i < size-1; i++ {
		for j := i + 1; j < size; j++ {
			if p.data[i] > p.data[j] {
				smaller[i]++
			} else {
				larger[i]++
			}
		}
	}

	if s.DebugMode() {
		fmt.Println(smaller)
		fmt.Println(larger)
	}

	count := 0

	for i := 0; i < size-2; i++ {
		s, l := smaller[i] >= 2, larger[i] >= 2

		if !s && !l {
			break
		}

		for j := i + 1; j < size-1; j++ {
			if s && smaller[j] >= 1 {
				count += smaller[j]
			}

			if l && larger[j] >= 1 {
				count += larger[j]
			}

			// fmt.Println(i, j, s, l, count)
		}
	}

	return count
}
