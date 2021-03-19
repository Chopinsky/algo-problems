package challenges

import "sort"

/**
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.



Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
Example 2:

Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= nums.length
*/

func mostCompetitive(nums []int, k int) []int {
	ans := make([]int, 0, k)
	size := len(nums)

	if k == size {
		return nums
	}

	for i, val := range nums {
		l := len(ans) - 1

		if i == 0 || l < 0 {
			ans = append(ans, val)
			continue
		}

		// need everything else to fill the array
		if k-1-l >= size-i {
			ans = append(ans, nums[i:]...)
			break
		}

		// larger element, append to the solution if it's
		// not yet full
		if val >= ans[l] {
			if l < k-1 {
				ans = append(ans, val)
			}

			continue
		}

		// find how many elements are going to be evicted
		idx := sort.Search(len(ans), func(j int) bool {
			return ans[j] > val
		})

		if k-idx >= size-i {
			end := k - size + i

			ans = ans[:end]
			ans = append(ans, nums[i:]...)

			break
		}

		ans = ans[:idx]
		ans = append(ans, val)
	}

	return ans
}
