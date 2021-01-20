package challenges

/**
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"
*/

func longestPalindrome(s string) string {
	size := len(s)
	if size == 0 {
		return s
	}

	p := make([]int, 2*size+1)
	b := make([]byte, 0, 2*size+1)

	for _, c := range s {
		b = append(b, '|')
		b = append(b, byte(c))
	}

	b = append(b, '|')

	// c - stores the center of the longest palindromic substring until now
	// r - stores the right boundary of the longest palindromic substring until now
	var c, r, max, pr, pl int

	for i := 0; i < 2*size+1; i++ {
		mirror := 2*c - i
		if i < r {
			p[i] = min(r-i, p[mirror])
		}

		rr := i + (1 + p[i])
		ll := i - (1 + p[i])

		for rr < 2*size+1 && ll >= 0 && b[ll] == b[rr] {
			p[i]++
			rr++
			ll--
		}

		if i+p[i] > r {
			c = i
			r = i + p[i]

			if p[i] > max {
				max = p[i]
				pr, pl = rr-1, ll+1
			}
		}
	}

	return string(s[pl/2 : pr/2])
}

func longestPalindrome1(s string) string {
	cnt := 1
	var l, r int
	size := len(s)

	for i := range s {
		if i > 0 {
			l0, r0 := palLen(s, i-1, i, size)
			if l0 >= 0 && r0 < size && r0-l0+1 > cnt {
				cnt = r0 - l0 + 1
				l, r = l0, r0
			}
		}

		l0, r0 := palLen(s, i-1, i+1, size)
		if l0 >= 0 && r0 < size && r0-l0+1 > cnt {
			cnt = r0 - l0 + 1
			l, r = l0, r0
		}

		// fmt.Println(i, l, r)
	}

	return s[l : r+1]
}

func palLen(s string, l, r, size int) (int, int) {
	for l >= 0 && r < size {
		if s[l] != s[r] {
			return l + 1, r - 1
		}

		l--
		r++
	}

	return l + 1, r - 1
}
