package bitorsub

import "sort"

// classic implementation of the 2d dp algo
func runDP2d(arr []uint) (uint, []uint) {
	arrLen := len(arr)

	dp := make([][]uint, arrLen)
	ans := make(map[uint]struct{})
	res := []uint{}

	for i := 0; i < arrLen; i++ {
		for j := i; j < arrLen; j++ {
			if i == j {
				dp[i] = make([]uint, arrLen)
				dp[i][j] = arr[j]
			} else {
				dp[i][j] = dp[i][j-1] | arr[j]
			}

			if _, ok := ans[dp[i][j]]; !ok {
				ans[dp[i][j]] = struct{}{}
				res = append(res, dp[i][j])
			}
		}
	}

	sort.Slice(res, func(i, j int) bool {
		return res[i] < res[j]
	})

	return uint(len(res)), res
}

// Flatten the 2d array to 1d -> use and dump, only keep track of last+current column
func runDP1d(arr []uint) (uint, []uint) {
	var curr, next map[uint]struct{}

	ans := make(map[uint]struct{})
	res := []uint{}

	curr = make(map[uint]struct{})
	for _, num := range arr {
		next = make(map[uint]struct{})
		next[num] = struct{}{}

		for val := range curr {
			temp := val | num
			if _, ok := next[temp]; !ok {
				next[temp] = struct{}{}

				if _, ok := ans[temp]; !ok {
					ans[temp] = struct{}{}
					res = append(res, temp)
				}
			}
		}

		curr = next
	}

	sort.Slice(res, func(i, j int) bool {
		return res[i] < res[j]
	})

	return uint(len(res)), res
}
