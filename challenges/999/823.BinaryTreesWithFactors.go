package challegnes

import "sort"

/**
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 109
*/

func numFactoredBinaryTrees(arr []int) int {
	sort.Ints(arr)

	mod := 1000000007
	nums := make(map[int]int)

	for _, num := range arr {
		nums[num] = 1
	}

	for i, n := range arr {
		for j := 0; j <= i; j++ {
			m := arr[j]
			product := n * m

			if nums[product] == 0 {
				continue
			}

			count := nums[n] * nums[m]
			if j != i {
				count *= 2
			}

			nums[product] += count
		}
	}

	count := 0
	for _, c := range nums {
		count = (count + c) % mod
	}

	return count % mod
}
