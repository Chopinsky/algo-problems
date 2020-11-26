package challenges

func uniqueMorseRepresentations(words []string) int {
	code := []string{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."}

	patterns := make(map[string]bool)

	for _, w := range words {
		c := ""

		for _, char := range w {
			c += code[int(char-'a')]
		}

		patterns[c] = true
	}

	return len(patterns)
}
