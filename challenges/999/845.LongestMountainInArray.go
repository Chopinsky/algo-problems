package challenges

/**
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3, There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
*/

func longestMountain(a []int) int {
	if len(a) < 3 {
		return 0
	}

	mt := 0
	curr := 0
	ans := 0

	for i := 1; i < len(a); i++ {
		if mt == 0 {
			if a[i] > a[i-1] {
				mt = 1
				curr = 2
			}

			continue
		} else if mt == 1 {
			if a[i] == a[i-1] {
				mt = 0
				curr = 0
			} else if a[i] < a[i-1] {
				mt = 2
				curr++
			} else {
				curr++
			}
		} else {
			if a[i] == a[i-1] {
				mt = 0
				if curr > ans {
					ans = curr
				}
			} else if a[i] > a[i-1] {
				if curr > ans {
					ans = curr
				}

				mt = 1
				curr = 2
			} else {
				curr++
			}
		}

		// fmt.Println(i, mt, curr, ans)
	}

	if mt == 2 && curr > ans {
		ans = curr
	}

	return ans
}
