package challenges

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
	if root == nil || (root.Left == nil && root.Right == nil) {
		return 0
	}

	return itLeft(root, true)
}

func itLeft(root *TreeNode, isLeft bool) int {
	if root.Left == nil && root.Right == nil {
		if isLeft {
			return root.Val
		}

		return 0
	}

	var sum int

	if root.Left != nil {
		sum += itLeft(root.Left, true)
	}

	if root.Right != nil {
		sum += itLeft(root.Right, false)
	}

	return sum
}
