package challenges

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

var maxVal = 1000000007

func minCameraCover(root *TreeNode) int {
	_, a, b := iterate(root)

	return min(a, b)
}

// 0: Strict ST -- all nodes below this node are covered, but not this node
// 1: Normal ST -- all nodes below and this node are covered, no camera at this node
// 2: Placed camera -- all nodes below this are covered, plus camera here
func iterate(root *TreeNode) (int, int, int) {
	if root == nil {
		// case 3 is illegal, max it out
		return 0, 0, maxVal
	}

	// child states
	l0, l1, l2 := iterate(root.Left)
	r0, r1, r2 := iterate(root.Right)

	// find the best combo for scenario 1 and 2
	l12 := min(l1, l2)
	r12 := min(r1, r2)

	// if this one is *not* covered but all sub-nodes are, left and
	// right nodes must be in state 1, i.e. no camera at the immediate
	// left *and* right children
	c0 := l1 + r1

	// left node has the camera + right node best scenario,
	// or right node has the camera + left node best scenario
	c1 := min(l2+r12, r2+l12)

	// placing the camera at this node, find the best scenario for both left and right nodes
	c2 := 1 + min(l0, l12) + min(r0, r12)

	return c0, c1, c2
}
