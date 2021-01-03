package challenges

import "fmt"

/**
Suppose you have n integers from 1 to n. We define a beautiful arrangement as an array that is constructed by these n numbers successfully if one of the following is true for the ith position (1 <= i <= n) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Given an integer n, return the number of the beautiful arrangements that you can construct.

Example 1:

Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Example 2:

Input: n = 1
Output: 1

Constraints:

1 <= n <= 15
*/

func countArrangement(n int) int {
	if n == 1 {
		return 1
	}

	cand := make(map[int][]int, n)

	for i := 1; i <= n; i++ {
		for j := 1; j <= 15; j++ {
			if i == j || (i > j && i%j == 0) || (i < j && j%i == 0) {
				cand[j] = append(cand[j], i)
			}
		}
	}

	// fmt.Println(cand)

	return iterateArr(cand, make(map[string]int), 0, 1, n)
}

func iterateArr(cand map[int][]int, cache map[string]int, seen, pos, n int) int {
	if pos > n {
		return 1
	}

	key := fmt.Sprint(seen, ",", pos)
	if val, ok := cache[key]; ok {
		return val
	}

	var count int

	for _, num := range cand[pos] {
		// the number is already used
		k := 1 << (num - 1)
		if k&seen > 0 {
			continue
		}

		count += iterateArr(cand, cache, seen|k, pos+1, n)
	}

	cache[key] = count
	return count
}
