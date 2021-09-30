package challenges

/**
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
*/

func pacificAtlantic(mat [][]int) [][]int {
	h := len(mat)
	if h == 0 {
		return nil
	}

	w := len(mat[0])
	ans := make([][]int, 0, h*w)
	dirs := []int{-1, 0, 1, 0, -1}

	pstack := make([][]int, 0, h+w)
	astack := make([][]int, 0, h+w)

	dp := make([][]int, h)
	for i := range dp {
		dp[i] = make([]int, w)

		if i == 0 {
			for j := range dp[i] {
				dp[i][j] |= 1
				pstack = append(pstack, []int{i, j})
			}
		} else {
			dp[i][0] |= 1
			pstack = append(pstack, []int{i, 0})
		}

		if i == h-1 {
			for j := range dp[i] {
				dp[i][j] |= 2
				astack = append(astack, []int{i, j})
			}
		} else {
			dp[i][w-1] |= 2
			astack = append(astack, []int{i, w - 1})
		}
	}

	// pacific iter
	var curr []int
	for len(pstack) > 0 {
		curr, pstack = pstack[0], pstack[1:]

		for i := 0; i < 4; i++ {
			x, y := curr[0]+dirs[i], curr[1]+dirs[i+1]

			// illegal point or already seen
			if x < 0 || x >= h || y < 0 || y >= w {
				continue
			}

			// can't flow there
			if dp[x][y]&1 > 0 || mat[x][y] < mat[curr[0]][curr[1]] {
				continue
			}

			// can flow
			dp[x][y] |= 1
			pstack = append(pstack, []int{x, y})
		}
	}

	// atlantic iter
	for len(astack) > 0 {
		curr, astack = astack[0], astack[1:]

		for i := 0; i < 4; i++ {
			x, y := curr[0]+dirs[i], curr[1]+dirs[i+1]

			// illegal point or already seen
			if x < 0 || x >= h || y < 0 || y >= w {
				continue
			}

			// can't flow there
			if dp[x][y]&2 > 0 || mat[x][y] < mat[curr[0]][curr[1]] {
				continue
			}

			// can flow
			dp[x][y] |= 2
			astack = append(astack, []int{x, y})
		}
	}

	// for i := range dp {
	//     fmt.Println(i, dp[i])
	// }

	// get answers
	for i := range dp {
		for j := range dp[i] {
			if dp[i][j] == 3 {
				ans = append(ans, []int{i, j})
			}
		}
	}

	return ans
}
