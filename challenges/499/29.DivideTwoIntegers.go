package challenges

/**
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:

Input: dividend = 0, divisor = 1
Output: 0

Example 4:

Input: dividend = 1, divisor = 1
Output: 1

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
*/

func divide(dividend int, divisor int) int {
	if dividend == 0 {
		return 0
	}

	sameSign := true

	if dividend < 0 {
		sameSign = !sameSign
		dividend = -dividend
	}

	if divisor < 0 {
		sameSign = !sameSign
		divisor = -divisor
	}

	ans := calcDiv(int64(dividend), int64(divisor))
	if !sameSign {
		ans = -ans
	}

	if ans < -2147483648 || ans > 2147483647 {
		ans = 2147483647
	}

	return int(ans)
}

func calcDiv(src, base int64) int64 {
	if src == 0 || src < base {
		return 0
	}

	if src == base {
		return 1
	}

	multi := int64(1)
	val := base

	for {
		if (val << 1) > src {
			break
		}

		val <<= 1
		multi <<= 1
	}

	return multi + calcDiv(src-val, base)
}
