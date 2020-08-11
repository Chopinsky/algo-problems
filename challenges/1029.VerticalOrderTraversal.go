package challenges

import (
	"fmt"
	"sort"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func verticalTraversal(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	nodes := traverse(root, 0, 0, []*node{})
	sort.Slice(nodes, func(i, j int) bool {
		if nodes[i].x != nodes[j].x {
			return nodes[i].x < nodes[j].x
		}

		if nodes[i].y != nodes[j].y {
			return nodes[i].y > nodes[j].y
		}

		return nodes[i].val < nodes[j].val
	})

	for _, v := range nodes {
		fmt.Println(v)
	}

	res := make([][]int, 0, len(nodes))
	curr := make([]int, 0, 8)
	x0 := nodes[0].x

	for _, v := range nodes {
		if v.x != x0 {
			res = append(res, curr)
			curr = make([]int, 0, 8)
			x0 = v.x
		}

		curr = append(curr, v.val)
	}

	if len(curr) > 0 {
		res = append(res, curr)
	}

	return res
}

type node struct {
	x   int
	y   int
	val int
}

func traverse(root *TreeNode, x, y int, store []*node) []*node {
	store = append(store, &node{
		x:   x,
		y:   y,
		val: root.Val,
	})

	if root.Left != nil {
		store = traverse(root.Left, x-1, y-1, store)
	}

	if root.Right != nil {
		store = traverse(root.Right, x+1, y-1, store)
	}

	return store
}
