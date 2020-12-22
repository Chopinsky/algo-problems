package challenges

/**
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lower-case English letters.
*/

func isInterleave(s1 string, s2 string, s3 string) bool {
	if len(s1)+len(s2) != len(s3) {
		return false
	}

	if s3 == "" {
		return true
	}

	size1, size2 := len(s1), len(s2)
	dp := make(map[int]bool, size1)

	for i, char := range s3 {
		if i == 0 {
			if size1 > 0 && s1[0] == byte(char) {
				dp[toKey(1, 0, size2+1)] = true
			}

			if size2 > 0 && s2[0] == byte(char) {
				dp[toKey(0, 1, size2+1)] = true
			}

			continue
		}

		if len(dp) == 0 {
			return false
		}

		tmp := make(map[int]bool, 2*len(dp))

		for key := range dp {
			n1, n2 := fromKey(key, size2+1)

			if n1 < size1 && s1[n1] == byte(char) {
				tmp[toKey(n1+1, n2, size2+1)] = true
			}

			if n2 < size2 && s2[n2] == byte(char) {
				tmp[toKey(n1, n2+1, size2+1)] = true
			}
		}

		dp = tmp
	}

	// fmt.Println(dp)

	return len(dp) > 0
}
