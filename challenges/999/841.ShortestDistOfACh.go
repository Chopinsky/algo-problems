package challenges

/**
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.

Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]

Constraints:

1 <= s.length <= 104
s[i] and c are lowercase English letters.
c occurs at least once in s.
*/

func shortestToChar(s string, c byte) []int {
	pos := make([]int, 0, len(s))

	for i, ch := range s {
		if byte(ch) == c {
			pos = append(pos, i)
		}
	}

	idx := 0
	l := len(pos)
	ans := make([]int, len(s))

	for i := range s {
		if i <= pos[idx] {
			ans[i] = pos[idx] - i
			continue
		}

		if idx == l-1 {
			ans[i] = i - pos[idx]
			continue
		}

		if i-pos[idx] >= pos[idx+1]-i {
			idx++
			ans[i] = pos[idx] - i
		} else {
			ans[i] = i - pos[idx]
		}
	}

	return ans
}
