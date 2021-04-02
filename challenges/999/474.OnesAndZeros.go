package challenges

/**
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
*/

func findMaxForm(strs []string, m int, n int) int {
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	for _, num := range strs {
		z, o := 0, 0
		for _, ch := range num {
			if ch == '0' {
				z++
			} else {
				o++
			}
		}

		// backwards -- update (i, j) not interferring later updates
		for i := m; i >= z; i-- {
			for j := n; j >= o; j-- {
				dp[i][j] = max(dp[i][j], dp[i-z][j-o]+1)
			}
		}
	}

	return dp[m][n]
}

func findMaxForm1(strs []string, m int, n int) int {
	dp := make([][]int, m+1)
	tmp := make([][]int, m+1)

	for i := range dp {
		dp[i] = make([]int, n+1)
		tmp[i] = make([]int, n+1)
	}

	for _, num := range strs {
		z, o := 0, 0
		for _, ch := range num {
			if ch == '0' {
				z++
			} else {
				o++
			}
		}

		for i := 0; i <= m; i++ {
			for j := 0; j <= n; j++ {
				tmp[i][j] = dp[i][j]
			}
		}

		for i := 0; i <= m; i++ {
			for j := 0; j <= n; j++ {
				if i+z > m || j+o > n {
					continue
				}

				if i == 0 && j == 0 {
					tmp[z][o] = max(dp[z][o], 1)
					continue
				}

				if dp[i][j] == 0 {
					continue
				}

				tmp[i+z][j+o] = max(dp[i+z][j+o], dp[i][j]+1)
			}
		}

		// fmt.Println(num, z, o)
		// fmt.Println(dp)
		// fmt.Println(tmp)

		dp, tmp = tmp, dp
	}

	//     for _, r := range dp {
	//         fmt.Println(r)
	//     }

	var cnt int
	for i := 0; i <= m; i++ {
		for j := 0; j <= n; j++ {
			if dp[i][j] > cnt {
				cnt = dp[i][j]
			}
		}
	}

	return cnt
}
