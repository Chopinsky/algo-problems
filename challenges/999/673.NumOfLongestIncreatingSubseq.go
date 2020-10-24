package challenges

import "fmt"

func findNumberOfLIS(nums []int) int {
	size := len(nums)
	if size <= 1 {
		return size
	}

	dp := make([][][]int, len(nums))
	dp[0] = append(dp[0], []int{nums[0], 1})
	top := 0

	for i := 1; i < size; i++ {
		val := nums[i]
		next := []int{val, 0}
		found := false

		for i := top; i >= 0; i-- {
			for j := range dp[i] {
				if dp[i][j][0] < val {
					found = true
					next[1] += dp[i][j][1]
				}
			}

			if found {
				dp[i+1] = append(dp[i+1], next)
				if i+1 > top {
					top = i + 1
				}

				break
			}
		}

		if !found {
			// the number forms a subsequence of itself
			next[1] = 1
			dp[0] = append(dp[0], next)
		}
	}

	fmt.Println(dp, top)

	sum := 0
	for i := range dp[top] {
		sum += dp[top][i][1]
	}

	return sum
}
