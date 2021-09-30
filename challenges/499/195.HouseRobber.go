package challenges

func rob(nums []int) int {
	if nums == nil || len(nums) == 0 {
		return 0
	}

	size := len(nums)
	if size == 1 {
		return nums[0]
	}

	if size == 2 {
		return max(nums[0], nums[1])
	}

	dp := make([][]int, size)

	for i := range dp {
		dp[i] = make([]int, 2)

		if i == 0 {
			dp[i][0] = nums[0]
		}

		if i == 1 {
			dp[i][0] = nums[1]
			dp[i][1] = nums[0]
		}
	}

	for i := 2; i < size; i++ {
		dp[i][0] = nums[i] + dp[i-1][1]
		dp[i][1] = max(dp[i-1][0], dp[i-1][1])
	}

	return max(dp[size-1][0], dp[size-1][1])
}
