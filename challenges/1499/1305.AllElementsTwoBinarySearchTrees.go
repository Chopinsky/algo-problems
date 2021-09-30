package challenges

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
	var s1, s2 []*TreeNode

	if root1 != nil {
		s1 = buildStack(root1, []*TreeNode{})
	}

	if root2 != nil {
		s2 = buildStack(root2, []*TreeNode{})
	}

	ans := make([]int, 0, len(s1)+len(s2))

	// fmt.Println(len(s1), len(s2))

	var l1, l2 int
	var node *TreeNode

	// use stack to flattern the recursive in-order traverse calls
	for len(s1) > 0 || len(s2) > 0 {
		l1, l2 = len(s1)-1, len(s2)-1

		if l2 < 0 || (l1 >= 0 && s1[l1].Val <= s2[l2].Val) {
			node = s1[l1]
			s1 = s1[:l1]

			ans = append(ans, node.Val)

			if node.Right != nil {
				s1 = buildStack(node.Right, s1)
			}
		} else {
			node = s2[l2]
			s2 = s2[:l2]

			ans = append(ans, node.Val)

			if node.Right != nil {
				s2 = buildStack(node.Right, s2)
			}
		}
	}

	return ans
}

func buildStack(root *TreeNode, stack []*TreeNode) []*TreeNode {
	stack = append(stack, root)

	if root.Left != nil {
		stack = buildStack(root.Left, stack)
	}

	return stack
}
