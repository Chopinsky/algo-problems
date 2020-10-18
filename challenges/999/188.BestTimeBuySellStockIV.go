package challenges

func maxProfitIV(k int, prices []int) int {
	if k == 0 || len(prices) <= 1 {
		return 0
	}

	n := len(prices)
	var profit int

	if 2*k > n {
		for i := 1; i < n; i++ {
			profit += max(0, prices[i]-prices[i-1])
		}

		return profit
	}

	// dp[i] is the profit at i-th day, since it's running
	// on k, which means the dp[i] is the max-profit if all
	// transactions happen on or before i-th day with at most
	// (k-1) transactions performed
	dp := make([]int, n)

	// starting from 1 trade, up to k trades
	for i := 0; i < k; i++ {
		next := make([]int, n)
		bestEntry := -prices[0]

		// find out the best profits with k-th trade, given the
		// max profits we can get from (k-1) trades that have
		// finished on or before j-th day
		for j := 1; j < n; j++ {
			// get a better buy prices along the way
			bestEntry = max(bestEntry, dp[j-1]-prices[j])

			// if we finished the trade on j-th day, update the max
			// profit: we either don't take the trade, or trade with
			// a previous best buy price
			next[j] = max(next[j-1], bestEntry+prices[j])
		}

		dp = next
	}

	return dp[n-1]
}

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
