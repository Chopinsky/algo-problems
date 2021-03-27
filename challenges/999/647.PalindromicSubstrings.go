package challenges

/**
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:

The input string length won't exceed 1000.
*/

func countSubstrings(s string) int {
	var count int
	ln := len(s)

	for i := 0; i < ln; i++ {
		for j := 0; i-j >= 0 && i+j < ln; j++ {
			if s[i+j] != s[i-j] {
				break
			}

			count++
		}
	}

	for i := 0; i < ln-1; i++ {
		for j := 0; i-j >= 0 && i+j+1 < ln; j++ {
			if s[i-j] != s[i+j+1] {
				break
			}

			count++
		}
	}

	return count
}
