package challenges

/**
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]
Output: 2

Example 3:

Input: nums = [1,1,1,1]
Output: 0

Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
*/

// find subsequence
func findLHS(nums []int) int {
	cnts := make(map[int]int)
	var ans int

	for _, val := range nums {
		cnts[val]++

		if cnts[val-1] > 0 && cnts[val]+cnts[val-1] > ans {
			ans = cnts[val] + cnts[val-1]
		}

		if cnts[val+1] > 0 && cnts[val]+cnts[val+1] > ans {
			ans = cnts[val] + cnts[val+1]
		}
	}

	return ans
}

// find subarray
func findLHS1(nums []int) int {
	var ans, cnt, hi, li int

	for i, val := range nums {
		if i == 0 {
			continue
		}

		if hi == li && (val == nums[hi]+1 || val == nums[li]-1) {
			if val == nums[hi]+1 {
				hi = i
			} else {
				li = i
			}

			cnt++
			if cnt > ans {
				ans = cnt
			}

			continue
		}

		if val == nums[hi] || val == nums[li] {
			cnt++
			if cnt > ans {
				ans = cnt
			}

			if hi == li {
				hi, li = i, i
			} else if val == nums[hi] {
				hi = i
			} else {
				li = i
			}

			continue
		}

		cnt = 1

		if val == nums[hi]+1 {
			li = li + 1
			hi = i
			continue
		}

		if val == nums[li]-1 {
			hi = hi + 1
			li = i
			continue
		}

		hi, li = i, i
	}

	return ans
}
