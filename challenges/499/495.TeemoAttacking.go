package challenges

func findPoisonedDuration(s []int, d int) int {
	size := len(s)
	if size == 0 {
		return 0
	}

	total := 0
	start, end := s[0], s[0]+d

	for i := 1; i < size; i++ {
		if s[i] > end {
			total += end - start
			start = s[i]
		}

		end = s[i] + d
	}

	total += end - start

	return total
}
