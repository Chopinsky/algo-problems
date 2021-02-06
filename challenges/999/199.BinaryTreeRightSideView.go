package challenges

/**
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
*/
func rightSideView(root *TreeNode) []int {
	store := make(map[int]int)
	lvl := view(root, store, 0)
	ans := make([]int, 0, lvl)

	for i := 0; i < lvl; i++ {
		ans = append(ans, store[i])
	}

	return ans
}

func view(root *TreeNode, store map[int]int, lvl int) int {
	if root == nil {
		return lvl
	}

	if _, ok := store[lvl]; !ok {
		store[lvl] = root.Val
	}

	lr := view(root.Right, store, lvl+1)
	ll := view(root.Left, store, lvl+1)

	return max(ll, lr)
}
