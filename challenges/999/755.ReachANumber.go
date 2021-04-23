package challenges

/**
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
*/

func reachNumber(target int) int {
	if target < 0 {
		target *= -1
	}

	if target <= 1 {
		return target
	}

	var k int

	for target > 0 {
		k++
		target -= k
	}

	if target%2 == 0 {
		return k
	}

	return k + 1 + k%2
}
