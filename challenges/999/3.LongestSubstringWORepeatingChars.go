package challenges

func lengthOfLongestSubstring(s string) int {
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
