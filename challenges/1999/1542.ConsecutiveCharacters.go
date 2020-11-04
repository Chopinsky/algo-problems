package challenges

func maxPower(s string) int {
	ch := s[0]
	count, best := 1, 0

	for i := 1; i < len(s); i++ {
		if s[i] != ch {
			if count > best {
				best = count
			}

			count = 1
			ch = s[i]
		} else {
			count++
		}
	}

	if count > best {
		best = count
	}

	return best
}
