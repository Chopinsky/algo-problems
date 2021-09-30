package challenges

func findTheDifference(s string, t string) byte {
	chars := make([]int, 26)

	for _, c := range s {
		chars[int(c-'a')]++
	}

	for _, c := range t {
		chars[int(c-'a')]--

		if chars[int(c-'a')] < 0 {
			return byte(c)
		}
	}

	return 0
}
