package challenges

/**
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
*/

// idea is the bottom-up dp: assuming we start with only 1 ballon: [0, i, n],
// which is easy, since nums[0] == nums[n] == 1, ans = nums[0]*nums[i]*nums[n]
// and then we calculate [0, j, i) and (i, j, n], and so on and so forth, until
// we fill all ballons back in place
func maxCoins(nums []int) int {
	size := len(nums)

	// rebuild array to include fake left / right bounds
	n := make([]int, size+2)
	copy(n[1:], nums)
	n[0], n[size+1] = 1, 1

	// build solution memo: memo[l][r] gives the max score for bursting
	// ballons in the range of (l, r), exclusively. Here l / r are padded
	memo := make([][]int, size+2)
	for i := range memo {
		memo[i] = make([]int, size+2)
	}

	return burst(memo, n, 0, size+1)
}

func burst(memo [][]int, nums []int, l, r int) int {
	// illegal range for: (l, r)
	if l+1 >= r {
		return 0
	}

	if memo[l][r] > 0 {
		return memo[l][r]
	}

	var ans int
	for i := l + 1; i < r; i++ {
		ans = max(ans, nums[l]*nums[i]*nums[r]+burst(memo, nums, l, i)+burst(memo, nums, i, r))
	}

	memo[l][r] = ans
	return ans
}
