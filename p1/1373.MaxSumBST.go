package p1

import (
	"fmt"
	s "go-problems/shared"
	"time"
)

// MSBProblems ...
type MSBProblems struct {
	set []*MSB
}

// Solve ...
func (p *MSBProblems) Solve() {
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

// MSB ...
type MSB struct {
	data   []int
	output int
}

// CreateMSB ...
func CreateMSB() s.Problem {
	set := make([]*MSB, 0, 4)

	set = append(set, &MSB{
		data:   []int{1, 4, 3, 2, 4, 2, 5, 0, 0, 0, 0, 0, 0, 4, 6},
		output: 20,
	})

	set = append(set, &MSB{
		data:   []int{4, 3, 0, 1, 2},
		output: 2,
	})

	set = append(set, &MSB{
		data:   []int{-4, -2, -5},
		output: 0,
	})

	set = append(set, &MSB{
		data:   []int{2, 1, 3},
		output: 6,
	})

	set = append(set, &MSB{
		data:   []int{5, 4, 8, 3, 0, 6, 3},
		output: 7,
	})

	return &MSBProblems{set}
}

var maxVal int = 0

func (p *MSB) solve() int {
	maxVal = 0
	p.walk(0, len(p.data))

	return maxVal
}

func (p *MSB) walk(idx, size int) (bool, int) {
	left, right := 2*idx+1, 2*idx+2
	val := p.data[idx]
	valid := true

	var lVal, rVal int
	lValid, rValid := true, true

	// the node is the leaf, always a valid BST
	if left >= size && right >= size {
		if val > maxVal {
			maxVal = val
		}

		if val >= 0 {
			return true, val
		}

		return true, 0
	}

	// left is a valid node
	if left < size && p.data[left] != 0 {
		lValid, lVal = p.walk(left, size)

		if p.data[idx] < p.data[left] || !lValid {
			valid = false
		}
	}

	// right is a valid node
	if right < size && p.data[right] != 0 {
		rValid, rVal = p.walk(right, size)

		if p.data[idx] > p.data[right] || !rValid {
			valid = false
		}
	}

	if s.DebugMode() {
		fmt.Println(idx, valid, lVal, rVal)
	}

	if !valid {
		return false, 0
	}

	val += lVal + rVal
	if val > maxVal {
		maxVal = val
	}

	if val > 0 {
		return true, val
	}

	return true, 0
}
