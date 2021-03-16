package challenges

func maxProfit(prices []int, fee int) int {
	not := 0
	has := 0

	// l := len(prices)
	// dp := make([][]int, l)

	for i, p := range prices {
		// dp[i] = make([]int, 2)

		if i == 0 {
			//dp[i][1] = -p - fee
			has = -p - fee
			continue
		}

		// dp[i][0] = max(dp[i-1][0], p+dp[i-1][1])
		// dp[i][1] = max(dp[i-1][1], dp[i-1][0] - p - fee)
		temp := not
		not = max(not, p+has)
		has = max(has, temp-p-fee)

	}

	// fmt.Println(dp)

	return not // dp[l-1][0]
}

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
