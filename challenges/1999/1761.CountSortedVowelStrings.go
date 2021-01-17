package challenges

func countVowelStrings(n int) int {
	counts := []int{1, 1, 1, 1, 1}
	n--

	for n > 0 {
		for i := 3; i >= 0; i-- {
			counts[i] += counts[i+1]
		}

		n--
	}

	var count int
	for _, val := range counts {
		count += val
	}

	return count
}
