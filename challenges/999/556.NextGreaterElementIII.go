package challenges

import "sort"

/**
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

Example 1:

Input: n = 12
Output: 21

Example 2:

Input: n = 21
Output: -1

Constraints:

1 <= n <= 231 - 1
*/

func nextGreaterElement(n int) int {
	d := make([]int, 0, 31)
	done := false
	top := (1 << 31) - 1
	var num int

	for n > 0 {
		num = n % 10
		n /= 10

		if len(d) > 0 && num < d[len(d)-1] {
			idx := 0
			for idx < len(d) && d[idx] <= num {
				idx++
			}

			num, d[idx] = d[idx], num
			n = n*10 + num

			sort.Ints(d)
			done = true

			break
		}

		d = append(d, num)
	}

	if !done {
		return -1
	}

	// fmt.Println(d)

	for i := 0; i < len(d); i++ {
		n = n*10 + d[i]
	}

	if n > top {
		return -1
	}

	return n
}
