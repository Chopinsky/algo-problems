package p0

func strongPasswordChecker(s string) int {
	if len(s) <= 4 {
		return 6 - len(s)
	}

	req := [3]int{0, 0, 0}
	t := charType(s[0])

	if t >= 0 {
		req[t]++
	}

	return update(s, req, s[0], 1, 0, 1, 2, len(s))
}

func update(s string, req [3]int, last byte, lastCount, corr, idx, length, size int) int {
	// one of the end-game senario
	if length == 20 {
		return calc(s, req, last, lastCount, corr, idx, length, size)
	}

	//todo: much more ...
	return 0
}

func calc(s string, req [3]int, last byte, lastCount, corr, idx, length, size int) int {
	rem := 0
	t := 0

	for _, val := range req {
		if val == 0 {
			rem++
		}
	}

	if rem == 0 {
		if s[idx] != last || lastCount < 2 {
			// requirements are met, and we don't have to change this char,
			// delete the remainder
			return corr + (size - 1) - idx
		}

		// scan the remainder of the string and determine if there can
		// be replacement for the char at `idx`
		del := 1

		for i := idx + 1; i < size; i++ {
			if s[i] != last {
				del--
				break
			}
		}

		// if del == 1, then we need to delete this last char in addition
		return corr + (size - 1) - idx + del
	}

	// find if we can use chars in the remainder of the string
	// to satisfy the requirements

	// assuming we need to change the last char
	del := 1

	for i := idx + 1; i < size; i++ {
		t = charType(s[i])

		// we can replace the last char, no need to delete/change it
		if req[t] == 0 {
			del--
			break
		}
	}

	// no replacement found, check if it needs to be deleted
	if del == 1 && (s[idx] != last || lastCount < 2) {
		//
		del--
	}

	// final outcome is the correction made + deleting remainders + if
	// the last char needs an update/deletion
	return corr + (size - 1) - idx + del
}

func charType(char byte) int {
	if char <= 'z' && char >= 'a' {
		return 0
	}

	if char <= 'Z' && char >= 'A' {
		return 1
	}

	if char <= '9' && char >= '0' {
		return 2
	}

	return -1
}
