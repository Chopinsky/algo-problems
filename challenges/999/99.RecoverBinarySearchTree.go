package challenges

func recoverTree(root *TreeNode) {
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
