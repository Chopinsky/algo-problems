package challenges

/**
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
*/

func minimumEffortPath(heights [][]int) int {
	h, w := len(heights), len(heights[0])
	if h == 1 && w == 1 {
		return 0
	}

	d := make([][]int, h)
	for i := range d {
		d[i] = make([]int, w)

		for j := range d[i] {
			if i != 0 || j != 0 {
				d[i][j] = 1000000007
			} else {
				d[i][j] = 0
			}
		}
	}

	dirs := []int{-1, 0, 1, 0, -1}
	hp := make(queue, 0, 64)
	hp.Push([]int{0, 0, 0})

	for hp.Len() > 0 {
		top := hp.Pop().([]int)
		x0, y0 := top[1], top[2]

		// fmt.Println(x0, y0, top[0], d[x0][y0])

		// already have a better solution
		if top[0] > d[x0][y0] || top[0] >= d[h-1][w-1] {
			continue
		}

		for i := 0; i < 4; i++ {
			x, y := x0+dirs[i], y0+dirs[i+1]

			if x < 0 || x >= h || y < 0 || y >= w || (x == 0 && y == 0) {
				continue
			}

			diff := max(abs(heights[x][y], heights[x0][y0]), top[0])
			if diff < d[x][y] {
				d[x][y] = diff
				hp.Push([]int{diff, x, y})
			}

			// if x == h-1 && y == w-1 {
			//   fmt.Println("destination:", diff)
			// }
		}
	}

	// for i := range d {
	//   fmt.Println(d[i])
	// }

	return d[h-1][w-1]
}
