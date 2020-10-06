package challenges

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func insertIntoBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		root = &TreeNode{
			Val:   val,
			Left:  nil,
			Right: nil,
		}

		return root
	}

	if val > root.Val {
		if root.Right != nil {
			insertIntoBST(root.Right, val)
		} else {
			root.Right = &TreeNode{
				Val:   val,
				Left:  nil,
				Right: nil,
			}
		}

		return root
	}

	if root.Left != nil {
		insertIntoBST(root.Left, val)
	} else {
		root.Left = &TreeNode{
			Val:   val,
			Left:  nil,
			Right: nil,
		}
	}

	return root
}
