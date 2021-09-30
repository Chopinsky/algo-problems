package challenges

import "sort"

/**
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1) and (x + 1, y - 1) respectively.

The vertical order traversal of a binary tree is a list of non-empty reports for each unique x-coordinate from left to right. Each report is a list of all nodes at a given x-coordinate. The report should be primarily sorted by y-coordinate from highest y-coordinate to lowest. If any two nodes have the same y-coordinate in the report, the node with the smaller value should appear earlier.

Return the vertical order traversal of the binary tree.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: Without loss of generality, we can assume the root node is at position (0, 0):
The node with value 9 occurs at position (-1, -1).
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2).
The node with value 20 occurs at position (1, -1).
The node with value 7 occurs at position (2, -2).

Example 2:

Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report [1,5,6], the node with value 5 comes first since 5 is smaller than 6.

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000

 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
*/
func verticalTraversal1(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	tree := make(map[int][][]int)
	l, r := iter(root, tree, 0, 0, 0, 0)

	// fmt.Println(l, r)
	// fmt.Println(tree)

	ans := make([][]int, 0, len(tree))
	for i := l; i <= r; i++ {
		sort.Slice(tree[i], func(x, y int) bool {
			if tree[i][x][0] == tree[i][y][0] {
				return tree[i][x][1] < tree[i][y][1]
			}

			return tree[i][x][0] < tree[i][y][0]
		})

		arr := make([]int, 0, len(tree[i]))
		for _, val := range tree[i] {
			arr = append(arr, val[1])
		}

		ans = append(ans, arr)
	}

	return ans
}

func iter(root *TreeNode, tree map[int][][]int, i, j, l, r int) (int, int) {
	var l0, r0 int
	tree[i] = append(tree[i], []int{j, root.Val})

	l = min(l, i)
	r = max(r, i)

	if root.Left != nil {
		l0, r0 = iter(root.Left, tree, i-1, j+1, l, r)
		l = min(l0, l)
		r = max(r0, r)
	}

	if root.Right != nil {
		l0, r0 = iter(root.Right, tree, i+1, j+1, l, r)
		l = min(l0, l)
		r = max(r0, r)
	}

	return l, r
}

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func min(a, b int) int {
	if a <= b {
		return a
	}

	return b
}
