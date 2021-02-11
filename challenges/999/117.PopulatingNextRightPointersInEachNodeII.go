package challenges

// TNode ...
type TNode struct {
	Val   int
	Left  *TNode
	Right *TNode
	Next  *TNode
}

/**
Given a binary tree


Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Example 1:

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
*/

func connectNodes(root *TNode) *TNode {
	return connNext(root, nil, true)
}

func connNext(root, parent *TNode, isRight bool) *TNode {
	if root == nil {
		return root
	}

	if parent != nil {
		if isRight || parent.Right == nil {
			next := parent.Next

			for next != nil {
				if next.Left != nil {
					root.Next = next.Left
					break
				}

				if next.Right != nil {
					root.Next = next.Right
					break
				}

				next = next.Next
			}
		} else {
			root.Next = parent.Right
		}
	}

	connNext(root.Right, root, true)
	connNext(root.Left, root, false)

	return root
}
