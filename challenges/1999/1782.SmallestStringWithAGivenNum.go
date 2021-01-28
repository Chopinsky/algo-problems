package challenges

/**
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

Example 1:

Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.

Example 2:

Input: n = 5, k = 73
Output: "aaszz"

Constraints:

1 <= n <= 105
n <= k <= 26 * n
*/

func getSmallestString(n int, k int) string {
	word := make([]byte, n)

	if k <= n+25 {
		for i := range word {
			if i != n-1 {
				word[i] = byte('a')
			} else {
				word[i] = byte('a') + byte(k-n)
			}
		}

		return string(word)
	}

	var idx int
	for idx < n {
		// fmt.Println(idx, k)

		if idx == n-1 {
			word[idx] = byte('a') + byte(k-1)
			// fmt.Println("a", idx, k, string(word[idx]))
			break
		}

		if 26*(n-idx-1)+1 >= k {
			word[idx] = byte('a')
			// fmt.Println("b", idx, k, string(word[idx]))
			k--
			idx++
			continue
		}

		word[idx] = byte('a') + byte(k-26*(n-1-idx)) - 1
		// fmt.Println("c", idx, k, string(word[idx]))

		k -= int(word[idx] - byte('a') + 1)
		idx++
	}

	return string(word)
}
