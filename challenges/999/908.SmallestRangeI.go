package challenges

func smallestRangeI(A []int, K int) int {
	if len(A) == 1 {
		return 0
	}

	// size := len(A)
	low, high := A[0], A[0]

	for _, val := range A {
		if val < low {
			low = val
		}

		if val > high {
			high = val
		}
	}

	lk, hk := high-K, low+K

	if lk <= hk {
		return 0
	}

	return lk - hk
}
