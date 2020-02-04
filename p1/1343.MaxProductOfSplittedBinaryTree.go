package p1

import (
	"fmt"
	s "go-problems/shared"
	"strconv"
	"time"
)

// MPSBTProblems ...
type MPSBTProblems struct {
	set []*MPSBT
}

// Solve ...
func (p *MPSBTProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 20; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 20 {
				s.Print(i, strconv.Itoa(p.output), strconv.Itoa(result))
			}
		}
	}

	fmt.Println("Algorithm took", time.Since(start))
}

// MPSBT ...
type MPSBT struct {
	data   []int
	output int
}

var mod = 1 // 10^9+7

// CreateMPSBT ...
func CreateMPSBT() s.Problem {
	set := make([]*MPSBT, 0, 4)

	set = append(set, &MPSBT{
		data:   []int{1, 2, 3, 4, 5, 6},
		output: 110,
	})

	set = append(set, &MPSBT{
		data:   []int{1, 0, 2, 3, 4, 0, 0, 5, 6},
		output: 90,
	})

	set = append(set, &MPSBT{
		data:   []int{2, 3, 9, 10, 7, 8, 6, 5, 4, 11, 1},
		output: 1025,
	})

	set = append(set, &MPSBT{
		data:   []int{1, 1},
		output: 1,
	})

	return &MPSBTProblems{set}
}

func (p *MPSBT) solve() int {
	size := len(p.data)
	treeSum := make([]int, size)

	for i := size - 1; i >= 0; i-- {
		sum := p.data[i]

		if 2*i+1 < size {
			sum += treeSum[2*i+1]
		}

		if 2*i+2 < size {
			sum += treeSum[2*i+2]
		}

		treeSum[i] = sum
	}

	if s.DebugMode() {
		fmt.Println(treeSum)
	}

	total := treeSum[0]
	max := 0

	for i := size - 1; i > 0; i-- {
		left, right := treeSum[i], total-treeSum[i]
		if left == 0 || right == 0 {
			continue
		}

		product := (left * right)
		if product > max {
			max = product
		}
	}

	return max
}
