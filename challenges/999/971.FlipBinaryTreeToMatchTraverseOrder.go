package challenges

/**
You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:


Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].

Example 1:

Input: root = [1,2], voyage = [2,1]
Output: [-1]
Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.

Example 2:

Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.

Example 3:

Input: root = [1,2,3], voyage = [1,2,3]
Output: []
Explanation: The tree's pre-order traversal already matches voyage, so no nodes need to be flipped.

Constraints:

The number of nodes in the tree is n.
n == voyage.length
1 <= n <= 100
1 <= Node.val, voyage[i] <= n
All the values in the tree are unique.
All the values in voyage are unique.

 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
*/
func flipMatchVoyage(root *TreeNode, voyage []int) []int {
	if root == nil {
		return nil
	}

	_, arr := flip(root, 0, voyage, []int{})
	if arr == nil {
		return []int{-1}
	}

	return arr
}

func flip(root *TreeNode, idx int, v, r []int) (int, []int) {
	if root == nil || r == nil {
		return -1, nil
	}

	if idx < 0 || idx >= len(v) || root.Val != v[idx] {
		return -1, nil
	}

	if root.Left == nil && root.Right == nil {
		return idx, r
	}

	last := idx

	if root.Left != nil && root.Right != nil && root.Left.Val != v[last+1] {
		r = append(r, root.Val)
		last, r = flip(root.Right, last+1, v, r)
		last, r = flip(root.Left, last+1, v, r)
	} else {
		if root.Left != nil {
			last, r = flip(root.Left, last+1, v, r)
		}

		if root.Right != nil {
			last, r = flip(root.Right, last+1, v, r)
		}
	}

	// fmt.Println(root, last, r)

	return last, r
}
