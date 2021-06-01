package challenges

import (
	"fmt"
	"sort"
)

/**
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
*/

// idea is to work up to the target sum, by adding a new number into
// the numbers candidate set: if in the previous subsequence, there
// exists a subset that can add up to a sum, then putting this new
// number into that subset will bring us to a new subset sum, and
// we will mark this sum as "reachable" (i.e. boolean value "true");
// goal is to add each number into the subsequence, and find out all
// subset sums that can be obtained, and check if we can ever get
// a subset sum equal to the half of the total set sum.
func canPartition(nums []int) bool {
	var sum int

	for _, v := range nums {
		sum += v
	}

	if sum%2 == 1 {
		return false
	}

	size := len(nums)
	tgt := sum / 2

	if nums[size-1] > tgt {
		return false
	}

	if nums[size-1] == tgt {
		return true
	}

	dp := make([]bool, tgt+1)
	dp[0] = true

	for _, val := range nums {
		// check if there's a subset whose sum plus val can bring us to the
		// target sum of `i`, and `i` must be greater or equal to val, since
		// sums are all positive, and subset are positive as well.
		for i := tgt; i >= val; i-- {
			dp[i] = dp[i] || dp[i-val]
		}
	}

	return dp[tgt]
}

func canPartition1(nums []int) bool {
	var sum int

	for _, v := range nums {
		sum += v
	}

	if sum%2 == 1 {
		return false
	}

	sort.Ints(nums)
	size := len(nums)

	if nums[size-1] > sum/2 {
		return false
	}

	if nums[size-1] == sum/2 {
		return true
	}

	cache := make(map[string]bool)

	return add(0, 0, sum/2, size, nums, cache)
}

func add(sum, idx, tgt, size int, nums []int, cache map[string]bool) bool {
	if sum > tgt || idx >= size {
		return false
	}

	if sum == tgt {
		return true
	}

	key := fmt.Sprint(sum, idx)
	if ans, ok := cache[key]; ok {
		return ans
	}

	if add(sum+nums[idx], idx+1, tgt, size, nums, cache) {
		cache[key] = true
		return true
	}

	ans := add(sum, idx+1, tgt, size, nums, cache)
	cache[key] = ans

	return ans
}
