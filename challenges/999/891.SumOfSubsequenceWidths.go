package challenges

import "sort"

// sum is:
//   S((i, j), j > i)_(2^(j-i-1) * (a[j] - a[i]))
//     ==>
//   S(i, 0, n-1)_((2^i - 2^(size-i-1)) * a[i])
func sumSubseqWidths(a []int) int {
	size := len(a)
	if size == 1 {
		return 0
	}

	if size == 2 {
		if a[0] < a[1] {
			return a[1] - a[0]
		}

		return a[0] - a[1]
	}

	sort.Ints(a)

	pow2 := make([]int, size)
	pow2[0] = 1

	sum := 0
	mod := 1000000007

	for i := 1; i < size; i++ {
		pow2[i] = (pow2[i-1] * 2) % mod
	}

	for l := 0; l < size; l++ {
		sum = (sum + (pow2[l]-pow2[size-1-l])*a[l]) % mod
	}

	return sum
}
