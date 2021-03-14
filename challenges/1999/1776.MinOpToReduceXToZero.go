package challenges

import "sort"

/**
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
*/

// max middle range
func minOperations(nums []int, x int) int {
	var sum int
	for _, val := range nums {
		sum += val
	}

	target := sum - x
	size := len(nums)

	if target < 0 {
		return -1
	}

	if target == 0 {
		return size
	}

	l, r := 0, 0
	sum = 0
	count := -1

	// fmt.Println("target:", target)

	for l < size && r < size {
		// fmt.Println(l, r, sum)

		for r < size && sum < target {
			sum += nums[r]
			r++
		}

		if sum == target {
			count = max(count, r-l)
		}

		for l <= r && l < size && sum >= target {
			sum -= nums[l]
			l++

			if sum == target {
				count = max(count, r-l)
			}
		}
	}

	if count < 0 {
		return -1
	}

	return size - count
}

// min head+tails
func minOperations1(nums []int, x int) int {
	presum := make([]int, len(nums)+1)

	for i, val := range nums {
		presum[i+1] = presum[i] + val
	}

	// fmt.Println(presum)
	l := len(nums)
	count := -1

	j := sort.SearchInts(presum, x)
	if j <= l && presum[j] == x {
		count = j
	}

	for i := l - 1; i >= 0; i-- {
		sum := x - (presum[l] - presum[i])
		if sum <= 0 {
			if sum == 0 && (count < 0 || l-i < count) {
				count = l - i
			}

			break
		}

		j = sort.SearchInts(presum, sum)
		if j > i {
			break
		}

		if presum[j] == sum && (count < 0 || l-i+j < count) {
			count = l - i + j
		}

		if count > 0 && l-i > count {
			break
		}
	}

	return count
}
