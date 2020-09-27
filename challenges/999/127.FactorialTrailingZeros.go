package challenges

func trailingZeroes(n int) int {
	count := 0
	base := 5

	for n/base >= 1 {
		count += (n / base)
		base *= 5
	}

	return count
}
