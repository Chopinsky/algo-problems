package challenges

func decodeString(s string) string {
	if len(s) < 4 {
		return s
	}

	ans, _ := decode(s, 0)

	return ans
}

func decode(s string, start int) (string, int) {
	ans := ""
	num := -1
	idx := start

	for idx < len(s) {
		c := s[idx]

		if c == '[' {
			// a starting point
			base, last := decode(s, idx+1)

			// append the subsection to the final result
			for j := 1; j <= num; j++ {
				ans += base
			}

			// reset: jump to the last char, which should be ']'
			idx = last
			num = -1
		} else if c == ']' {
			break
		} else if c >= '0' && c <= '9' {
			// a number char
			if num < 0 {
				num = int(c - '0')
			} else {
				num = num*10 + int(c-'0')
			}
		} else {
			// a alphabet char
			ans += s[idx : idx+1]
		}

		idx++
	}

	return ans, idx
}
