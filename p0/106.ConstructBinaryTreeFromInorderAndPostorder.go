package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// CBTFIPProblems ...
type CBTFIPProblems struct {
	set []*CBTFIP
}

// Solve ...
func (p *CBTFIPProblems) Solve() {
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

// CBTFIP ...
type CBTFIP struct {
	data   []int
	post   []int
	output int
}

// CreateCBTFIP ...
func CreateCBTFIP() s.Problem {
	set := make([]*CBTFIP, 0, 4)

	set = append(set, &CBTFIP{
		data:   []int{9, 3, 15, 20, 7},
		post:   []int{9, 15, 7, 20, 3},
		output: 0,
	})

	return &CBTFIPProblems{set}
}

func (p *CBTFIP) solve() int {
	return 0
}

// TreeNode ...
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(io []int, po []int) *TreeNode {
	if io == nil || po == nil || len(po) == 0 {
		return nil
	}

	last := len(po) - 1
	rVal := po[last]

	if last == 0 {
		return &TreeNode{
			Val:   rVal,
			Left:  nil,
			Right: nil,
		}
	}

	pivot := -1

	for i := range io {
		if io[i] == rVal {
			pivot = i
			break
		}
	}

	var lio, lpo, rio, rpo []int

	if pivot == 0 {
		rio = io[1:]
		rpo = po[:last]
	} else if pivot == last {
		lio = io[:pivot]
		lpo = po[:last]
	} else {
		lio = io[:pivot]
		lpo = po[:pivot]

		rio = io[pivot+1:]
		rpo = po[pivot:last]
	}

	return &TreeNode{
		Val:   rVal,
		Left:  buildTree(lio, lpo),
		Right: buildTree(rio, rpo),
	}
}
