package challenges

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findTilt(root *TreeNode) int {
	if root == nil {
		return 0
	}

	_, t := walkTree(root)
	return t
}

func walkTree(root *TreeNode) (int, int) {
	var ls, lt, rs, rt int

	if root.Left != nil {
		ls, lt = walkTree(root.Left)
	}

	if root.Right != nil {
		rs, rt = walkTree(root.Right)
	}

	return root.Val + ls + rs, diffAbs(ls, rs) + lt + rt
}

func diffAbs(a, b int) int {
	if a >= b {
		return a - b
	}

	return b - a
}
