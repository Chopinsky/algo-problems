package challenges

import (
	"fmt"
	"sort"
)

/**
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Example 4:

Input: coins = [1], amount = 1
Output: 1

Example 5:

Input: coins = [1], amount = 2
Output: 2

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
*/

func coinChange(coins []int, amount int) int {
	dp := make([]int, amount+1)
	for i := range dp {
		dp[i] = -1
	}

	sort.Ints(coins)

	for i := range dp {
		if i == 0 {
			dp[i] = 0
			continue
		}

		for _, c := range coins {
			if c > i {
				break
			}

			if dp[i-c] < 0 {
				continue
			}

			if dp[i] < 0 {
				dp[i] = dp[i-c] + 1
			} else {
				dp[i] = min(dp[i], dp[i-c]+1)
			}
		}
	}

	return dp[amount]
}

func coinChange1(coins []int, amount int) int {
	if amount == 0 {
		return 0
	}

	sort.Ints(coins)

	dp := make(map[string]int)
	max := make([]bool, len(coins))
	cnt := calcCoins(coins, max, amount, dp)

	return cnt
}

func calcCoins(coins []int, max []bool, amount int, dp map[string]int) int {
	if amount == 0 {
		return 0
	}

	if len(coins) == 0 {
		return -1
	}

	k := fmt.Sprintf("%d,%d", len(coins), amount)
	if val, ok := dp[k]; ok {
		return val
	}

	if len(coins) == 1 {
		cnt := amount / coins[0]
		rem := amount - cnt*coins[0]

		if rem != 0 {
			dp[k] = -1
			return -1
		}

		dp[k] = cnt
		return cnt
	}

	last := len(coins) - 1

	var cnt int
	total := -1

	for cnt*coins[last] <= amount {
		cnt++
	}

	for cnt >= 0 {
		next := calcCoins(coins[:last], max, amount-cnt*coins[last], dp)

		// fmt.Println(cnt, next, total)

		if next >= 0 && (total < 0 || total > next+cnt) {
			total = next + cnt

			if next == 0 {
				break
			}
		}

		cnt--
	}

	// fmt.Println(coins, amount, total)

	dp[k] = total
	return total
}
