package challenges

/**
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.

Example 4:

Input: s = "1"
Output: 1

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
*/

func numDecodings(s string) int {
	raw := []byte(s)
	l := len(s)

	arr := make([]int, l)
	for i := range raw {
		arr[i] = int(raw[i] - '0')
	}

	if l < 2 {
		if l == 1 && arr[0] == 0 {
			return 0
		}

		return l
	}

	// return reduce(arr)
	dp := make([]int, l)

	for i := l - 1; i >= 0; i-- {
		if arr[i] == 0 {
			if i < l-1 && arr[i+1] == 0 {
				break
			}

			continue
		}

		if i == l-1 {
			dp[i] = 1
			continue
		}

		dp[i] = dp[i+1]
		if arr[i]*10+arr[i+1] > 26 {
			continue
		}

		if i < l-2 {
			dp[i] += dp[i+2]
		} else {
			dp[i]++
		}

		if arr[i] != 0 && dp[i] == 0 {
			break
		}
	}

	return dp[0]
}
