package challenges

import "sort"

/**
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:

Input: nums = [1,2,3,4]
Output: 0

Example 3:

Input: nums = [1]
Output: 0

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105


Follow up: Can you solve it in O(n) time complexity?
*/

func findUnsortedSubarray(nums []int) int {
	size := len(nums)
	if size <= 1 {
		return 0
	}

	maxPos := -1
	initPos := -1
	lastPos := -1

	for i, val := range nums {
		if i == 0 {
			continue
		}

		if val < nums[i-1] {
			if initPos < 0 {
				initPos = i - 1

				idx := sort.SearchInts(nums[:i-1], val+1)
				if idx <= i-1 {
					initPos = idx
				}
			} else {
				idx := sort.SearchInts(nums[:initPos], val+1)
				if idx <= initPos {
					initPos = idx
				}
			}

			if maxPos < 0 || nums[i-1] > nums[maxPos] {
				maxPos = i - 1
			}

			lastPos = i
		}

		if maxPos >= 0 && val < nums[maxPos] {
			idx := sort.SearchInts(nums[:initPos], val+1)
			if idx <= initPos {
				initPos = idx
			}

			lastPos = i
		}
	}

	// fmt.Println("final:", initPos, lastPos, maxPos, minPos)

	if initPos < 0 {
		return 0
	}

	if lastPos < 0 {
		lastPos = size - 1
	}

	return lastPos - initPos + 1
}
