package challenges

/**
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1.

Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.

Constraints:

1 <= n <= 10^5
*/

func concatenatedBinary(n int) int {
	mod := int64(1000000007)
	base, shift := int64(1), int64(1)
	th := int64((1 << shift) - 1)
	var ans int64

	for base <= int64(n) {
		ans = (ans<<shift + base) % mod
		base++

		if base > th {
			th = (th << 1) | 1
			shift++
		}
	}

	return int(ans % mod)
}
