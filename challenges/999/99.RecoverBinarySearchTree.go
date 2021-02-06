package challenges

/**
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

Example 1:

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
*/

func recoverTree(root *TreeNode) {
	n1, n2 := searchNode(root)
	if n1 == nil || n2 == nil {
		return
	}

	// fix the tree
	n1.Val, n2.Val = n2.Val, n1.Val
}

func searchNode(root *TreeNode) (n1, n2 *TreeNode) {
	stack := []*TreeNode{}
	curr := root
	var pre *TreeNode

	// use in-order traverse to discover the abnomality
	for curr != nil || len(stack) > 0 {
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}

		curr = stack[len(stack)-1]

		// found abnormalty, make sure
		if pre != nil && pre.Val > curr.Val {
			if n1 == nil {
				n1 = pre
			}

			n2 = curr
		}

		// set previous value, it must be smaller than everything
		// in the stack
		pre = curr

		// now move on to the next larger number in the "sorted array"
		// version of the tree
		curr = curr.Right

		// pop and move on
		stack = stack[:len(stack)-1]
	}

	// done
	return
}

func recoverTree1(root *TreeNode) {
	if root == nil {
		return
	}

	nl, nr := findNode(root.Left, nil, root, false), findNode(root.Right, root, nil, false)

	if nl != nil && nr != nil {
		nl = findNode(root.Left, nil, root, true)
		nr = findNode(root.Right, root, nil, true)
		nl.Val, nr.Val = nr.Val, nl.Val
		return
	}

	if nl != nil {
		fix(root.Left, nil, root)
	} else if nr != nil {
		fix(root.Right, root, nil)
	}
}

func findNode(root, l, r *TreeNode, first bool) *TreeNode {
	if root == nil {
		return nil
	}

	var n *TreeNode
	var nl, nr *TreeNode

	if (l != nil && root.Val < l.Val) || (r != nil && root.Val > r.Val) {
		n = root

		if first {
			return n
		}
	}

	if root.Left != nil {
		nl = findNode(root.Left, l, root, first)
	}

	if root.Right != nil {
		nr = findNode(root.Right, root, r, first)
	}

	// 2 misplaced nodes, exchange and done
	if nl != nil && nr != nil {
		nl = findNode(root.Left, l, root, true)
		nr = findNode(root.Right, root, r, true)

		if r != nil && nl.Val > r.Val && nr.Val > r.Val {
			return nl
		}

		if l != nil && nl.Val < l.Val && nr.Val < l.Val {
			return nr
		}

		nl.Val, nr.Val = nr.Val, nl.Val
		return nil
	}

	if nl != nil {
		return nl
	}

	if nr != nil {
		return nr
	}

	return n
}

func fix(root, l, r *TreeNode) bool {
	if root == nil {
		return false
	}

	if l != nil && root.Val < l.Val {
		n := findNode(root.Left, nil, root, true)
		if n == nil {
			n = findNode(root.Right, root, nil, true)
		}

		if n != nil && n.Val < root.Val {
			exchange(n, l)
		} else {
			exchange(root, l)
		}
	}

	if r != nil && root.Val > r.Val {
		n := findNode(root.Left, nil, root, true)
		if n == nil {
			n = findNode(root.Right, root, nil, true)
		}

		if n != nil && n.Val > root.Val {
			exchange(n, r)
		} else {
			exchange(root, r)
		}
	}

	if fix(root.Left, l, root) || fix(root.Right, root, r) {
		return true
	}

	return false
}

func exchange(a, b *TreeNode) {
	a.Val, b.Val = b.Val, a.Val
}
