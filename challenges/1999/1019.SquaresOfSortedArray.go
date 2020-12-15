package challenges

/**
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
*/

func sortedSquares(nums []int) []int {
	if nums[0] >= 0 {
		for i := range nums {
			nums[i] *= nums[i]
		}

		return nums
	}

	l := findNeg(nums)
	r := l + 1
	ans := make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		if l < 0 {
			ans[i] = nums[r] * nums[r]
			r++

			continue
		}

		if r >= len(nums) {
			ans[i] = nums[l] * nums[l]
			l--

			continue
		}

		if smaller(nums[l], nums[r]) {
			ans[i] = nums[l] * nums[l]
			l--

			continue
		}

		ans[i] = nums[r] * nums[r]
		r++
	}

	return ans
}

func smaller(a, b int) bool {
	if a < 0 {
		a = -a
	}

	if b < 0 {
		b = -b
	}

	return a < b
}

func findNeg(nums []int) int {
	l, r := 0, len(nums)

	for l < r {
		m := (l + r) / 2

		if nums[m] == 0 {
			l = m
			break
		}

		if nums[m] < 0 {
			l = m + 1
		} else {
			r = m - 1
		}
	}

	if l >= len(nums) {
		l = len(nums) - 1
	}

	for nums[l] >= 0 {
		l--
	}

	return l
}
