package challenges

func rob1(nums []int) int {
	size := len(nums)
	if size == 1 {
		return nums[0]
	}

	if size == 2 {
		return max(nums[0], nums[1])
	}

	return max(rob0(nums[:size-1], size-1), rob0(nums[1:], size-1))
}

func rob0(nums []int, size int) int {
	dp := make([][]int, size)
	for i := range dp {
		dp[i] = make([]int, 2)
		if i == 0 {
			dp[0][0] = nums[0]
		}

		if i == 1 {
			dp[1][0] = nums[1]
			dp[1][1] = max(dp[0][0], dp[0][1])
		}
	}

	for i := 2; i < size; i++ {
		dp[i][0] = nums[i] + max(dp[i-2][0], dp[i-2][1])
		dp[i][1] = max(dp[i-1][0], dp[i-1][1])
	}

	return max(dp[size-1][0], dp[size-1][1])
}
