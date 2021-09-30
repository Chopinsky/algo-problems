package challenges

/**
====================
Problem:

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3

====================
Solution:

Essentially a problem to find the starting point of a closed circle in
a linked list (i.e. i -> nums[i] is a link).

Use fast/slow pointers, where fast pointer walks 2 steps while slow
pointer walks 1 step on each iteration for the first part. They meet
in a circle with `b` nodes, and the duplicate number (the starting nodes
) is at `a`, then they meet at node `k`, we have the following:

2 * (a + k) = (a + b) + k

which gives: a = b - k

Then slow from 0, fast from k, after walking a steps (and meet at a), we have
slow @ 0 + a = a; fast @ k + a = k + (b - k) = b, and after finishing the full circle, fast is at a (the stating point) again.

see Floyd's Tortoise and Hare (Cycle Detection)
*/

func findDuplicate(nums []int) int {
	slow, fast := nums[0], nums[nums[0]]
	for slow != fast {
		slow, fast = nums[slow], nums[nums[fast]]
	}

	slow, fast = nums[0], nums[fast]
	for slow != fast {
		slow, fast = nums[slow], nums[fast]
	}

	return slow
}

func findDuplicate1(nums []int) int {
	n := len(nums)

	if n <= 5 {
		return fastCount(nums, 1, n)
	}

	l, r := 1, n
	mc, lc, rc := 0, 0, 0
	var m, lt, rt int

	for l < r {
		m = (l + r) / 2
		lt, rt = m-l, r-m

		// fmt.Println(l, m, r)

		for _, val := range nums {
			if val == m {
				mc++
			} else if val < m && val >= l {
				lc++
			} else if val > m && val <= r {
				rc++
			} else {
				continue
			}

			if mc > 1 {
				return m
			}

			if lc > lt {
				r = m - 1
				break
			}

			if rc > rt {
				l = m + 1
				break
			}
		}

		// fmt.Println(l, lc, lt, ";", r, rc, rt, ";", m, mc)

		if r-l <= 5 {
			return fastCount(nums, l, r)
		}

		// reset
		mc, lc, rc = 0, 0, 0
	}

	return l
}

func fastCount(src []int, l, r int) int {
	cache := make([]int, r-l+1)

	for _, val := range src {
		if val < l || val > r {
			continue
		}

		if cache[val-l] != 0 {
			return val
		}

		cache[val-l] = 1
	}

	return l
}
