package challenges

// TreeNode ...
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, sum int) int {
	if root == nil {
		return 0
	}

	// presums from root to the current node: sum total -> count
	preSums := make(map[int]int)

	// always legal to need 0 values from presums, it's the empty array -- starts from the current node
	preSums[0] = 1

	return countSums(root, preSums, 0, sum)
}

func countSums(root *TreeNode, preSums map[int]int, currSum, sum int) int {
	currSum += root.Val
	want := currSum - sum

	total := 0
	if cnt, ok := preSums[want]; ok {
		// if there're path to a (grand)parent node that meets the sum, such that by
		// removing this path, the remainder in the path sum to the target
		total += cnt
	}

	// now add the current sum total to the presums in the path
	preSums[currSum]++

	if root.Left != nil {
		total += countSums(root.Left, preSums, currSum, sum)
	}

	if root.Right != nil {
		total += countSums(root.Right, preSums, currSum, sum)
	}

	// backtrace
	preSums[currSum]--

	return total
}

func countSums1(root *TreeNode, levels []int, l, sum, count int) int {
	levels[l] = root.Val + levels[l-1]

	for i := 0; i < l; i++ {
		if levels[l]-levels[i] == sum {
			count++
		}
	}

	if root.Left != nil {
		count = countSums1(root.Left, levels, l+1, sum, count)
	}

	if root.Right != nil {
		count = countSums1(root.Right, levels, l+1, sum, count)
	}

	levels[l] = 0
	return count
}
