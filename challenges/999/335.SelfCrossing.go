package challenges

/**
You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:

┌───┐
│   │
└───┼──>
    │

Input: [2,1,1,2]
Output: true

Example 2:

┌──────┐
│      │
│
│
└────────────>

Input: [1,2,3,4]
Output: false

Example 3:

┌───┐
│   │
└───┼>

Input: [1,1,1,1]
Output: true
*/

func isSelfCrossing(x []int) bool {
	if x == nil || len(x) <= 3 {
		return false
	}

	point := []int{0, 0}

	for i := 0; i < len(x); i++ {
		if i >= 3 && x[i] >= x[i-2] && x[i-1] <= x[i-3] {
			// fmt.Println("meet 3:", i, x[i])
			return true
		}

		if i >= 5 && x[i-2] >= x[i-4] && x[i-3] >= x[i-1] && x[i]+x[i-4] >= x[i-2] && x[i-1]+x[i-5] >= x[i-3] {
			// fmt.Println("meet 5:", i, x[i])
			return true
		}

		if i%4 == 0 {
			point[1] += x[i]
		} else if i%3 == 0 {
			point[0] += x[i]
		} else if i%2 == 0 {
			point[1] -= x[i]
		} else {
			point[0] -= x[i]
		}

		// fmt.Println("point:", point)

		if point[0] == 0 && point[1] == 0 {
			return true
		}
	}

	return false
}
