package challenges

/**
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true


Note:

1 <= N <= 10^9
*/

func reorderedPowerOf2(n int) bool {
	if n < 10 {
		return n == 1 || n == 2 || n == 4 || n == 8
	}

	d := make([]int, 10)
	large := 0
	count := 0
	low, high := 1, 1

	for n > 0 {
		rem := n % 10
		d[rem]++

		if rem > large {
			large = rem
		}

		n /= 10
		low *= 10
		high *= 10
		count++
	}

	low /= 10
	high--

	base := 1
	nn := make([]int, 10)
	for base <= high {
		base <<= 1
		if base < low {
			continue
		}

		disect(base, nn)
		done := true

		for i := range d {
			if d[i] != nn[i] {
				done = false
				break
			}
		}

		if done {
			return true
		}
	}

	// fmt.Println(d, count, low, high)

	return false
}

func disect(n int, nums []int) {
	for i := range nums {
		nums[i] = 0
	}

	for n > 0 {
		rem := n % 10
		nums[rem]++
		n /= 10
	}
}
