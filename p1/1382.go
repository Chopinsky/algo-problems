package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// BBSTProblems ...
type BBSTProblems struct {
	set []*BBST
}

// Solve ...
func (p *BBSTProblems) Solve() {
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

// BBST ...
type BBST struct {
	data   []int
	output []int
}

// CreateBBST ...
func CreateBBST() s.Problem {
	set := make([]*BBST, 0, 4)

	set = append(set, &BBST{
		data:   []int{1, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 4},
		output: []int{2, 1, 3, 0, 0, 0, 4},
	})

	return &BBSTProblems{set}
}

func (p *BBST) solve() []int {
	size := len(p.data)
	vals := make([]int, 0, size)
	stack := make([]int, 0, 4*size)

	stack = append(stack, 0)
	for len(stack) > 0 {
		last := len(stack) - 1
		left := 2*stack[last] + 1

		if left < size && p.data[left] > 0 {
			stack = append(stack, left)
			continue
		}

		vals = append(vals, p.data[stack[last]])
		right := 2*stack[last] + 2

		if right < size && p.data[right] > 0 {
			stack[last] = right
			continue
		} else {
			stack = stack[:last]
		}
	}

	if s.DebugMode() {
		fmt.Println(vals)
	}

	tree := make([]int, size)
	tree = buildTree(tree, vals, size, 0, 0, len(vals)-1)
	trimPos := size - 1

	for trimPos >= 0 {
		if tree[trimPos] == 0 {
			trimPos--
			continue
		}

		trimPos++
		break
	}

	return tree[:trimPos]
}

func buildTree(tree, src []int, size, pos, left, right int) []int {
	if left > right {
		return tree
	}

	mid := (left + right) / 2
	tree[pos] = src[mid]

	nLeft, nRight := 2*pos+1, 2*pos+2

	if nLeft < size {
		tree = buildTree(tree, src, size, nLeft, left, mid-1)
	}

	if nRight < size {
		tree = buildTree(tree, src, size, nRight, mid+1, right)
	}

	return tree
}
