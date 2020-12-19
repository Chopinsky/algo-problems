package challenges

func increasingTriplet(nums []int) bool {
	s1, s2 := -1, -1
	s1s, s2s := false, false
	lastValid := -1
	ls := false

	for _, val := range nums {
		if (s1s && s2s && val > s2) || (ls && val > lastValid) {
			// fmt.Println("found", s1, s2, val)
			return true
		}

		if !s2s {
			s2 = val
			s2s = true
			// fmt.Println("set s2", s1, s2, val)
			continue
		}

		if !s1s {
			if val <= s2 {
				s2 = val
				// fmt.Println("set s1 partial", s1, s2, val)
				continue
			}

			s1 = s2
			s2 = val
			s1s = true
			// fmt.Println("set s1", s1, s2, val)
			continue
		}

		if val < s1 {
			if !ls || s2 < lastValid {
				ls = true
				lastValid = s2
			}

			s2s = false
			s2 = -1
			s1 = val
			// fmt.Println("update s1", s1, s2, val)
			continue
		}

		if val < s2 && val > s1 {
			s2 = val
			// fmt.Println("update s2", s1, s2, val)
			continue
		}
	}

	return false
}
