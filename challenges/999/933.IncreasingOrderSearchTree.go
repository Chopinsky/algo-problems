package challenges

/**
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:

Input: root = [5,1,7]
Output: [1,null,5,null,7]
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func increasingBST(root *TreeNode) *TreeNode {
	h, _ := traverse(root)
	return h
}

func traverse(root *TreeNode) (*TreeNode, *TreeNode) {
	if root == nil {
		return root, root
	}

	// fmt.Println(root.Val)
	var h, t *TreeNode

	if root.Right != nil {
		hr, tr := traverse(root.Right)
		root.Right = hr
		t = tr
	} else {
		t = root
	}

	if root.Left != nil {
		hl, tl := traverse(root.Left)
		root.Left = nil
		tl.Right = root
		h = hl
	} else {
		h = root
	}

	return h, t
}
