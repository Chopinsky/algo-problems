package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// BSTNDProblems ...
type BSTNDProblems struct {
	set []*BSTND
}

// Solve ...
func (p *BSTNDProblems) Solve() {
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

// BSTND ...
type BSTND struct {
	data   []int
	output int
}

// CreateBSTND ...
func CreateBSTND() s.Problem {
	set := make([]*BSTND, 0, 4)

	set = append(set, &BSTND{
		data:   []int{},
		output: 0,
	})

	return &BSTNDProblems{set}
}

func (p *BSTND) solve() int {
	deleteNode(nil, 0)
	return 0
}

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return nil
	}

	if root.Val == key {
		if root.Left == nil && root.Right == nil {
			return nil
		}

		if root.Left == nil && root.Right != nil {
			return root.Right
		}

		if root.Left != nil && root.Right == nil {
			return root.Left
		}

		// in order delete
		root.Val, root.Right = traceDelete(root.Right)
		return root
	}

	if root.Val > key && root.Left != nil {
		root.Left = deleteNode(root.Left, key)
	}

	if root.Val < key && root.Right != nil {
		root.Right = deleteNode(root.Right, key)
	}

	return root
}

func traceDelete(root *TreeNode) (int, *TreeNode) {
	if root.Left == nil && root.Right == nil {
		return root.Val, nil
	}

	var val int
	if root.Left != nil {
		val, root.Left = traceDelete(root.Left)
		return val, root
	}

	return root.Val, root.Right
}
