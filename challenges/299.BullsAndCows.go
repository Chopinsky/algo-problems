package challenges

func getHint(secret string, guess string) string {
	a, b := 0, 0
	base := make([]int, 10)
	pos := make([]bool, len(secret))

	for _, char := range secret {
		base[char-'0']++
	}

	for i, char := range secret {
		if byte(char) == guess[i] {
			a++
			pos[i] = true
			base[char-'0']--
		}
	}

	for i, char := range guess {
		if pos[i] {
			continue
		}

		if base[char-'0'] > 0 {
			b++
			base[char-'0']--
		}
	}

	return strconv.Itoa(a) + "A" + strconv.Itoa(b) + "B"
}
