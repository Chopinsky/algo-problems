package challenges

/**
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
*/

func numberOfArithmeticSlices(a []int) int {
	if len(a) < 3 {
		return 0
	}

	l, r := 0, 2
	ans := 0

	for l < len(a)-2 {
		diff := a[l+1] - a[l]
		if a[r]-a[r-1] != diff {
			l++
			r++
			continue
		}

		// [l, l+1, r]
		ans++
		if r == len(a)-1 && l == r-2 {
			break
		}

		for r < len(a)-1 {
			r++
			if a[r]-a[r-1] != diff {
				l = r - 2
				break
			}

			ans += (r - l - 1)

			if r == len(a)-1 {
				return ans
			}
		}

		// fmt.Println(l, r, ans)
	}

	return ans
}
