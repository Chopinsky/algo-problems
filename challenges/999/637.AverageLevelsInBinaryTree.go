package challenges

/**
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]

Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:
The range of node's value is in the range of 32-bit signed integer.

 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
*/
func averageOfLevels(root *TreeNode) []float64 {
	sum := make(map[int][2]int)
	iter(root, sum, 0)

	avg := make([]float64, len(sum))
	for i := range avg {
		avg[i] = float64(sum[i][0]) / float64(sum[i][1])
	}

	return avg
}

func iter(root *TreeNode, sum map[int][2]int, level int) {
	if root == nil {
		return
	}

	if _, ok := sum[level]; !ok {
		sum[level] = [2]int{0, 0}
	}

	arr := sum[level]
	arr[0] += root.Val
	arr[1]++
	sum[level] = arr

	iter(root.Left, sum, level+1)
	iter(root.Right, sum, level+1)
}
