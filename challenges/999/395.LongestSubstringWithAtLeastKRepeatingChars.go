package challenges

import (
	"fmt"
	"sort"
)

/**
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
*/

func longestSubstring(s string, k int) int {
	if k == 1 {
		return len(s)
	}

	var num int
	counts := make([]int, 26)

	for _, c := range s {
		idx := int(c - 'a')
		if counts[idx] == 0 {
			num++
		}

		counts[idx]++
	}

	var idx, jdx, l, r, uc, lc, long int
	var rc []int

	for u := 1; u <= num; u++ {
		l, r = 0, 1
		lc, uc = 0, 1
		rc = make([]int, 26)
		idx = int(s[0] - 'a')

		rc[idx]++

		// outmost: slide right bound
		for r < len(s) {
			idx = int(s[r] - 'a')

			if rc[idx] == 0 {
				uc++

				// inner: slide left bound
				for uc > u && l < r {
					jdx = int(s[l] - 'a')
					if rc[jdx] == k {
						lc--
					}

					rc[jdx]--
					l++

					if rc[jdx] == 0 {
						uc--
					}
				}
			}

			rc[idx]++
			if rc[idx] == k {
				lc++
			}

			if lc == uc && r-l+1 > long {
				long = r - l + 1
			}

			r++
		}
	}

	return long
}

func longestSubstring1(s string, k int) int {
	if k == 1 {
		return len(s)
	}

	counts := make([][]int, 26)
	for i, char := range s {
		idx := int(char - 'a')
		if counts[idx] == nil {
			counts[idx] = []int{idx, i, 1}
		} else {
			counts[idx][2]++
		}
	}

	sort.Slice(counts, func(i, j int) bool {
		if counts[i] == nil {
			return false
		}

		if counts[j] == nil {
			return true
		}

		return counts[i][2] > counts[j][2]
	})

	chars := make(map[int][]int)
	for _, c := range counts {
		if c == nil || c[2] < k {
			break
		}

		chars[c[0]] = c
	}

	if len(chars) == 0 {
		return 0
	}

	fmt.Println(chars)
	var long int

	for _, c := range chars {
		counts := make(map[int]int)
		for key, c := range chars {
			counts[key] = c[2]
		}

		l := findLS(s, c[1], k, counts)
		fmt.Println(c[0], l)

		if l > long {
			long = l
		}
	}

	return long
}

func findLS(s string, start, k int, chars map[int]int) int {
	runningCount := make(map[int]int)
	left := -1
	var long int

	for i := start; i < len(s); i++ {
		c := s[i]
		idx := int(c - 'a')

		// hitting the end of the substring
		if runningCount[idx] == 0 && chars[idx] < k {
			if left >= 0 {
				done := true

				for _, v := range runningCount {
					if v < k {
						done = false
						break
					}
				}

				if done {
					// fmt.Println("new long", i, left)

					l := i - left
					if l > long {
						long = l
					}
				}
			}

			left = -1
			runningCount = make(map[int]int)

			continue
		}

		if left < 0 {
			left = i
		}

		chars[idx]--
		runningCount[idx]++
	}

	if left >= 0 {
		done := true

		for _, v := range runningCount {
			if v < k {
				done = false
				break
			}
		}

		if done {
			l := len(s) - left
			if l > long {
				long = l
			}
		}
	}

	return long
}
