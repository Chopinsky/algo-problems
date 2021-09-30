package challenges

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rob2(root *TreeNode) int {
	r, nr := robChild(root)
	return max(r, nr)
}

func robChild(root *TreeNode) (int, int) {
	if root == nil {
		return 0, 0
	}

	lr, lnr := robChild(root.Left)
	rr, rnr := robChild(root.Right)

	r := root.Val + lnr + rnr
	nr := max(lr, lnr) + max(rr, rnr)

	return r, nr
}
