package challenges

/**
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
*/

func lengthOfLongestSubstring(s string) int {
	if s == "" {
		return 0
	}

	var ans, l int
	chars := make(map[rune]int)

	for i, c := range s {
		if pos, ok := chars[c]; ok && pos+1 > l {
			l = pos + 1
		}

		chars[c] = i
		// fmt.Println(i, string(c), l)

		if i-l+1 > ans {
			ans = i - l + 1
		}
	}

	return ans
}

func lengthOfLongestSubstring1(s string) int {
	if len(s) <= 1 {
		return len(s)
	}

	size := len(s)
	set := make(map[byte]int)
	set[s[0]]++

	l, r := 0, 0
	c := s[r]
	ans := 1

	for l < size {
		if size-l < ans {
			break
		}

		for r < size {
			r++
			if r == size {
				break
			}

			c = s[r]
			set[c]++

			if set[c] < 2 {
				continue
			}

			if r-l > ans {
				ans = r - l
			}

			break
		}

		if r == size {
			if r-l > ans {
				ans = r - l
			}

			break
		}

		for s[l] != s[r] {
			set[s[l]]--
			l++
		}

		if l != r {
			set[s[l]]--
			l++

			if r-l+1 > ans {
				ans = r - l + 1
			}
		}

		// fmt.Println(l, r)
	}

	return ans
}
