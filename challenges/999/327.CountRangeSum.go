package challenges

/**
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3

Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
*/

func countRangeSum(nums []int, lower int, upper int) int {
	size := len(nums)
	presum := make([]int, size+1)

	for i, v := range nums {
		presum[i+1] = presum[i] + v
	}

	return mergeCount(presum, 0, size+1, lower, upper)
}

// idea is to hack into the merge process: when merging, the order
// between any number in the left-half and the number in the
// right-half are still correct, and this is the ground for the
// counting -- we merge with compares, and which will tell us the
// correct counts as well.
func mergeCount(presum []int, start, end, lower, upper int) int {
	if end-start <= 1 {
		return 0
	}

	m := (start + end) / 2

	// after this, all [m, end) presums are sorted by values, and they're all to the right
	// of [start, m), meaning presum[j] - presum[i] is always the range sum for `j` in the right
	// half, and `i` in left-half
	count := mergeCount(presum, start, m, lower, upper) + mergeCount(presum, m, end, lower, upper)

	il, iu, j := m, m, m
	next := make([]int, 0, end-start)

	for i := start; i < m; i++ {
		// get to the presum that's larger or equal than the lower bound; `il`
		// for the new i will surely be equal or larger than the last `il` value
		for il < end && presum[il]-presum[i] < lower {
			il++
		}

		// get to the presum that's larger than the upper bound; 'iu' for the new
		// i will surely be equal or larger than the last `iu` value
		for iu < end && presum[iu]-presum[i] <= upper {
			iu++
		}

		// the diff is the number of right ends of the ranges
		// in the [lower, upper] range for i-th element
		count += (iu - il)

		// fmt.Println(start, end, count, iu, il)

		// gather all presums in the right half, that's also smaller than i-th in the left-half
		for j < end && presum[j] < presum[i] {
			next = append(next, presum[j])
			j++
		}

		// now add the i-th presum to the cache
		next = append(next, presum[i])
	}

	// done, now merge: cache are sorted, and contains numbers that are smaller than the largest
	// number to the last of the presum in the left
	copy(presum[start:], next)

	return count
}
