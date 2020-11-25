package challenges

import "sort"

func partitionLabels(s string) []int {
	dp := make([][]int, 26)
	for i := range dp {
		dp[i] = []int{-1, -1}
	}

	for i, char := range s {
		j := char - 'a'

		if dp[j][0] == -1 {
			dp[j][0] = i
		}

		dp[j][1] = i
	}

	sort.Slice(dp, func(i, j int) bool {
		return dp[i][0] < dp[j][0]
	})

	idx := 0
	for dp[idx][0] == -1 {
		idx++
	}

	start := 0
	curr := dp[idx][1]
	ans := make([]int, 0, 26)

	// fmt.Println(dp[idx:])

	for i := idx + 1; i < 26; i++ {
		if dp[i][0] < curr {
			if dp[i][1] > curr {
				curr = dp[i][1]
			}

			continue
		}

		ans = append(ans, curr-start+1)

		start = dp[i][0]
		curr = dp[i][1]
	}

	ans = append(ans, curr-start+1)
	return ans
}
