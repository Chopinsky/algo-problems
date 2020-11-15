package challenges

/**
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
*/
func rangeSumBST(root *TreeNode, low int, high int) int {
	if root == nil {
		return 0
	}

	sum := 0
	if root.Val <= high && root.Val >= low {
		sum += root.Val
	}

	if root.Left != nil && root.Val > low {
		sum += rangeSumBST(root.Left, low, high)
	}

	if root.Right != nil && root.Val < high {
		sum += rangeSumBST(root.Right, low, high)
	}

	return sum
}
