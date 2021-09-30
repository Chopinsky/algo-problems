package challenges

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxAncestorDiff(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return walkTree(root, root.Val, root.Val, 0)
}

func walkTree(root *TreeNode, max, min, diff int) int {
	if root == nil {
		return diff
	}

	d := maxVal(abs(max, root.Val), abs(min, root.Val))

	if d > diff {
		diff = d
	}

	if root.Val > max {
		max = root.Val
	}

	if root.Val < min {
		min = root.Val
	}

	d0 := walkTree(root.Left, max, min, d)
	d1 := walkTree(root.Right, max, min, d)

	return maxVal(d, maxVal(d0, d1))
}

func abs(a, b int) int {
	if a >= b {
		return a - b
	}

	return b - a
}

func maxVal(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
