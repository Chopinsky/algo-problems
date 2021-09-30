package challenges

import "strings"

/**
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
*/

func originalDigits(s string) string {
	nums := map[int]string{
		0: "zero",
		1: "one",
		2: "two",
		3: "three",
		4: "four",
		5: "five",
		6: "six",
		7: "seven",
		8: "eight",
		9: "nine",
	}

	iter := [][]int{
		[]int{0, int('z')},
		[]int{2, int('w')},
		[]int{6, int('x')},
		[]int{7, int('s')},
		[]int{8, int('g')},
		[]int{4, int('u')},
		[]int{5, int('f')},
		[]int{1, int('o')},
		[]int{9, int('i')},
		[]int{3, int('t')},
	}

	chars := make(map[int]int)
	for _, ch := range s {
		chars[int(ch)]++
	}

	// fmt.Println(chars, nums, iter)

	count := make([]int, 10)
	for _, set := range iter {
		if c, ok := chars[set[1]]; ok && c > 0 {
			// fmt.Println(set, c)

			count[set[0]] += c
			for _, ch := range nums[set[0]] {
				chars[int(ch)] -= c
			}
		}
	}

	var ans strings.Builder
	for i, c := range count {
		for c > 0 {
			ans.WriteRune(rune('0' + i))
			c--
		}
	}

	return ans.String()
}
