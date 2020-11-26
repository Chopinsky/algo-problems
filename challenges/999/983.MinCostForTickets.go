package challenges

import "fmt"

/**
==================
Problem:

In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

=================
Example:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
*/
func mincostTickets(days []int, costs []int) int {
	last := len(days) - 1
	dp := make([]int, days[last]+1)
	d := make(map[int]bool)

	for _, v := range days {
		d[v] = true
	}

	var d1, d7, d30 int

	for i := days[0]; i <= days[last]; i++ {
		if !d[i] {
			dp[i] = dp[i-1]
			continue
		}

		d1 = dp[i-1] + costs[0]

		if i >= 7 {
			d7 = dp[i-7] + costs[1]
		} else {
			d7 = costs[1]
		}

		if i >= 30 {
			d30 = dp[i-30] + costs[2]
		} else {
			d30 = costs[2]
		}

		dp[i] = min3(d1, d7, d30)
	}

	fmt.Println(dp)

	return dp[len(dp)-1]
}

func min3(a, b, c int) int {
	if a > b {
		a = b
	}

	if a > c {
		a = c
	}

	return a
}
