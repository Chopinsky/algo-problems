package challenges

func sortArrayByParity(A []int) []int {
	size := len(A)
	if size <= 1 {
		return A
	}

	l, r := 0, size-1
	for l < r {
		for l < size && A[l]%2 == 0 {
			l++
		}

		for r > 0 && A[r]%2 == 1 {
			r--
		}

		if l < r {
			A[l], A[r] = A[r], A[l]
		}
	}

	return A
}
