package challenges

import "sort"

func smallestRangeII(A []int, K int) int {
	if len(A) == 1 {
		return 0
	}

	sort.Ints(A)
	size := len(A)

	baseline := A[size-1] - A[0]
	low := make([]int, size)
	high := make([]int, size)

	for i, val := range A {
		low[i] = val - K
		high[i] = val + K
	}

	for i := 0; i < size-1; i++ {
		l := min(high[0], low[i+1])
		h := max(high[i], low[size-1])

		if h-l < baseline {
			baseline = h - l
		}
	}

	return baseline
}
