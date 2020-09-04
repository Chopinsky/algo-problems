package challenges

import (
	"sort"
)

func maxChunksToSorted(arr []int) int {
	size := len(arr)
	if size == 1 {
		return 1
	}

	stack := make([]int, 0, size)
	for _, val := range arr {
		if len(stack) == 0 {
			stack = append(stack, val)
			continue
		}

		// push values that are in ascending orders, ignoring numbers
		// that needs to shuffle, hence creating the "sliding windows"
		if val >= stack[len(stack)-1] {
			stack = append(stack, val)
		}
	}

	maxInt := 1000000001
	ans, min := 0, maxInt

	for i := size - 1; i >= 0; i-- {
		num := arr[i]

		// keep updating the bench
		if num < min {
			min = num
		}

		// pop the top if it's in good order
		if len(stack) != 0 && stack[len(stack)-1] == num {
			stack = stack[:len(stack)-1]
		}

		// check if we're at the "head" of the current sliding window
		if len(stack) == 0 || stack[len(stack)-1] <= min {
			min = maxInt
			ans++
		}
	}

	return ans
}

func maxChunksToSorted1(arr []int) int {
	size := len(arr)
	if size == 1 {
		return 1
	}

	dp := make([][]int, 0, size)
	for i, val := range arr {
		dp = append(dp, []int{val, i})
	}

	sort.Slice(dp, func(i, j int) bool {
		if dp[i][0] == dp[j][0] {
			return dp[i][1] < dp[j][1]
		}

		return dp[i][0] < dp[j][0]
	})

	// fmt.Println("dp:", dp)

	ans := 0
	end := dp[0][1]

	for i := 1; i < size; i++ {
		if i <= end {
			if dp[i][1] > end {
				end = dp[i][1]
			}

			continue
		}

		ans++
		end = dp[i][1]
	}

	ans++
	return ans
}
