package challenges

import "sort"

/**
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
*/

// make sure taller envelops are ranked lower if width is the same,
// such that they won't be counted twice
func maxEnvelopes(env [][]int) int {
	sort.Slice(env, func(i, j int) bool {
		if env[i][0] == env[j][0] {
			return env[i][1] > env[j][1]
		}

		return env[i][0] < env[j][0]
	})

	// fmt.Println(next)

	nums := make([]int, 0, len(env))
	ans := 0

	for i, e := range env {
		if i > 0 && e[0] == env[i-1][0] && e[1] == env[i-1][1] {
			continue
		}

		pos := sort.SearchInts(nums, e[1])

		if pos == len(nums) {
			nums = append(nums, e[1])
		} else {
			nums[pos] = e[1]
		}

		if pos+1 > ans {
			ans = pos + 1
		}
	}

	return ans
}
