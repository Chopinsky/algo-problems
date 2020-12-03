package challenges

/**
Given a positive integer N, return the number of positive integers less than or equal to N that have at least 1 repeated digit.

Example 1:

Input: 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.

Example 2:

Input: 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.

Example 3:

Input: 1000
Output: 262
*/

// the idea is to count all the digits with unique digits in them,
// then substract N from this number, will give the rest: those
// with at least 1 repeating digit
func numDupDigitsAtMostN(N int) int {
	if N < 11 {
		return 0
	}

	if N < 100 {
		return N / 11
	}

	digits := []int{}
	n := N

	for n > 0 {
		digits = append(digits, n%10)
		n /= 10
	}

	size := len(digits)
	count := 0

	// the leading number can only choose from [1, 9], hence 9 times;
	// the following numbers can choose from [0, 9], and compound use
	// b(9, i-1)
	for i := 1; i < size; i++ {
		count += 9 * compound(9, i-1)
	}

	// fmt.Println("pre:", count, digits)

	// handle the numbers with prefix from `size-1` to `0`, note that
	// for i == size-1, i.e. the leading number, we can only choose
	// from [1, digits[i]-1], otherwise, we can choose from [0, digits[j]-1]
	// as long as it's not the number in the existing prefix.
	//
	// top to bottom series: 8XXX, 87XX, 872X, 8725
	seen := make(map[int]bool)
	for i := size - 1; i >= 0; i-- {
		num := digits[i]
		if num == 0 {
			if seen[0] {
				break
			}

			seen[0] = true
			continue
		}

		j := 0
		if i == size-1 {
			j = 1
		}

		base := compound(10+i-size, i)

		// fmt.Println("mid:", base, num, j)

		for j < num {
			if !seen[j] {
				count += base
			}

			j++
		}

		// we won't make a unique number with this prefix
		if seen[num] {
			break
		}

		// mark the prefix of the higher level digits
		seen[num] = true
	}

	if len(seen) == size {
		count++
	}

	// fmt.Println("final:", count, size, len(seen))

	return N - count
}

func compound(m, n int) int {
	ans := 1

	for n > 0 {
		ans *= m
		m--
		n--
	}

	return ans
}

func numDupDigitsAtMostN1(N int) int {
	if N < 11 {
		return 0
	}

	if N < 100 {
		return N / 11
	}

	digits := []int{}
	n := N + 1

	for n > 0 {
		digits = append(digits, n%10)
		n /= 10
	}

	size := len(digits)
	count := 0

	// numbers with unique digits for all numbers < 10^size
	for i := 0; i < size; i++ {
		if i > 0 {
			count += 9 * a(9, i-1)
		}

		if i < size/2 {
			digits[i], digits[size-1-i] = digits[size-1-i], digits[i]
		}
	}

	// count numbers with digits as prefix
	seen := make(map[int]bool)
	for i := 0; i < size; i++ {
		j := 0

		if i == 0 {
			j = 1
		}

		for j < digits[i] {
			if !seen[j] {
				count += a(9-i, size-i-1)
			}

			j++
		}

		if seen[digits[i]] {
			break
		}

		seen[digits[i]] = true
	}

	// fmt.Println(count, digits, size)

	return N - count
}

func a(m, n int) int {
	if n == 0 {
		return 1
	}

	return a(m, n-1) * (m - n + 1)
}
