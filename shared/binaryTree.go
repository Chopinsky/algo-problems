package shared

// TreeNode ...
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// MakeNode ...
func MakeNode(val int) *TreeNode {
	return &TreeNode{
		Val:   val,
		Left:  nil,
		Right: nil,
	}
}

// Insert ...
func (n *TreeNode) Insert(val int) bool {
	if val == n.Val {
		return false
	}

	if val < n.Val {
		if n.Left != nil {
			return n.Left.Insert(val)
		}

		n.Left = MakeNode(val)
		return true
	}

	if n.Right != nil {
		return n.Right.Insert(val)
	}

	n.Right = MakeNode(val)
	return true
}

// Floor ... first number smaller than val
func (n *TreeNode) Floor(val int) *TreeNode {
	if val == n.Val {
		return n
	}

	if val < n.Val {
		if n.Left != nil {
			return n.Left.Floor(val)
		}

		return nil
	}

	var r *TreeNode
	if r.Right != nil {
		r = n.Right.Floor(val)
	}

	if r == nil || val < r.Val {
		return n
	}

	return r
}

// Ceil ... first number larger than val
func (n *TreeNode) Ceil(val int) *TreeNode {
	if val == n.Val {
		return n
	}

	if val > n.Val {
		if n.Right != nil {
			return n.Right.Ceil(val)
		}

		return nil
	}

	var l *TreeNode
	if n.Left != nil {
		l = n.Left.Ceil(val)
	}

	if l == nil || val > l.Val {
		return n
	}

	return l
}

// Min ...
func (n *TreeNode) Min() int {
	if n.Left == nil {
		return n.Val
	}

	return n.Left.Min()
}

// Max ...
func (n *TreeNode) Max() int {
	if n.Right == nil {
		return n.Val
	}

	return n.Right.Max()
}

// Delete ...
func (n *TreeNode) Delete(val int) *TreeNode {
	if val < n.Val {
		if n.Left != nil {
			n.Left = n.Left.Delete(val)
		}

		return n
	}

	if val > n.Val {
		if n.Right != nil {
			n.Right = n.Right.Delete(val)
		}

		return n
	}

	if n.Left == nil && n.Right == nil {
		return nil
	}

	if n.Left == nil || n.Right == nil {
		if n.Left == nil {
			return n.Right
		}

		return n.Left
	}

	// both n.Left and n.Right are non-null, replace the
	// value with the minimum in the right sub-tree, and
	// remove the min-value-node from the sub-tree
	n.Val = n.Right.Min()
	n.Right = n.Right.Delete(n.Val)

	return n
}
