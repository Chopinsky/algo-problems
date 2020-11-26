package challenges

func buddyStrings(a string, b string) bool {
	if len(a) != len(b) {
		return false
	}

	pos := make([]int, 0, 2)
	chars := make([]int, 26)
	swapped := false

	for i, c := range a {
		chars[int(c-'a')]++

		if c == rune(b[i]) {
			continue
		}

		if len(pos) == 0 {
			pos = append(pos, i)
		} else if len(pos) == 1 {
			if a[pos[0]] == b[i] && a[i] == b[pos[0]] {
				swapped = true
				pos = append(pos, i)
			} else {
				return false
			}
		} else {
			return false
		}
	}

	if len(pos) == 1 {
		return false
	}

	if !swapped {
		for _, c := range chars {
			if c > 1 {
				return true
			}
		}
	}

	return swapped
}
