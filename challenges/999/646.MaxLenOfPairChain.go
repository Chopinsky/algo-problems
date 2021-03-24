package challenges

import "sort"

/**
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]

Note:
The number of given pairs will be in the range [1, 1000].
*/

func findLongestChain(pairs [][]int) int {
	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i][1] == pairs[j][1] {
			return pairs[i][0] < pairs[j][0]
		}

		return pairs[i][1] < pairs[j][1]
	})

	ans, curr := 0, pairs[0][0]-1

	// idea is that if the curr represents the best solution pair
	// ending with "curr" as the bounds.
	for _, p := range pairs {
		if curr < p[0] {
			curr = p[1]
			ans++
		}
	}

	/* Alt solution 1:
	var pos int
	ans := 1
	l := len(pairs)
	dp := make([]int, l)
	bounds := make([]int, 0, l)

	for i, p := range pairs {
		if len(bounds) > 0 {
			pos = sort.SearchInts(bounds, p[0])
		} else {
			pos = 0
		}

		// extend from the longest subsequence ending with pairs[pos-1][1]
		if pos > 0 {
			dp[i] = dp[pos-1] + 1
		} else {
			dp[i] = 1
		}

		// check if the previous subsequence can form a longer one, if so,
		// we use the last one
		if i > 0 && dp[i-1] > dp[i] {
			dp[i] = dp[i-1]
		}

		bounds = append(bounds, p[1])
	}
	*/

	/* Alt solution 2:
	ans := 1
	l := len(pairs)
	dp := make([]int, l)

	for i, p := range pairs {
	  dp[i] = 1
	  for j := 0; j < i && pairs[j][1] < p[0]; j++ {
	    if dp[j]+1 > dp[i] {
	      dp[i] = dp[j]+1
	    }
	  }

	  if dp[i] > ans {
	    ans = dp[i]
	  }
	}
	*/

	return ans
}
