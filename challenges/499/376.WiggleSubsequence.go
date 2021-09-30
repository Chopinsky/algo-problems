package challenges

/**
Given an integer array nums, return the length of the longest wiggle sequence.

A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.
A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

Example 2:

Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Example 3:

Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000


Follow up: Could you solve this in O(n) time?
*/

func wiggleMaxLength(nums []int) int {
	n := len(nums)
	if n < 2 {
		return n
	}

	curr := nums[0]
	i := 1
	cnt := 1

	for i < n {
		if nums[i] == curr {
			i++
			continue
		}

		if nums[i] > curr {
			for i < n && nums[i] >= nums[i-1] {
				i++
			}

			cnt++
		} else {
			for i < n && nums[i] <= nums[i-1] {
				i++
			}

			cnt++
		}

		curr = nums[i-1]
	}

	return cnt
}

func wiggleMaxLength1(nums []int) int {
	l := len(nums)
	if l <= 2 {
		if l == 2 && nums[0] == nums[1] {
			return 1
		}

		return l
	}

	dp := make([][]int, l)
	desc := make([]int, 0, l)
	asc := make([]int, 0, l)
	var j, max int

	for i, n := range nums {
		dp[i] = make([]int, 2)

		if i == 0 {
			desc = append(desc, i)
			asc = append(asc, i)
			dp[i][0], dp[i][1] = 1, 1
			continue
		}

		j = len(desc) - 1
		for j >= 0 {
			if nums[desc[j]] > n {
				break
			}

			j--
		}

		desc = desc[:(j + 1)]
		max = 0

		for j >= 0 {
			if dp[desc[j]][1] > max {
				max = dp[desc[j]][1]
			}

			j--
		}

		dp[i][0] = max + 1
		desc = append(desc, i)

		j = len(asc) - 1
		for j >= 0 {
			if nums[asc[j]] < n {
				break
			}

			j--
		}

		asc = asc[:(j + 1)]
		max = 0

		for j >= 0 {
			if dp[asc[j]][0] > max {
				max = dp[asc[j]][0]
			}

			j--
		}

		dp[i][1] = max + 1
		asc = append(asc, i)
	}

	// fmt.Println(dp, l)

	if dp[l-1][0] > dp[l-1][1] {
		return dp[l-1][0]
	}

	return dp[l-1][1]
}
