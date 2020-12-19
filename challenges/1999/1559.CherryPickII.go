package challenges

func cherryPickup(grid [][]int) int {
	h, w := len(grid), len(grid[0])

	dp := make([][][]int, h)
	for i := range dp {
		dp[i] = make([][]int, w)

		for j := range dp[i] {
			dp[i][j] = make([]int, w)

			for k := range dp[i][j] {
				dp[i][j][k] = -1
			}
		}
	}

	dp[0][0][w-1] = grid[0][0] + grid[0][w-1]
	dirs := [][]int{
		{-1, -1}, {-1, 0}, {-1, 1},
		{0, -1}, {0, 0}, {0, 1},
		{1, -1}, {1, 0}, {1, 1},
	}

	for i := 1; i < h; i++ {
		for j := 0; j < w; j++ {
			for k := j; k < w; k++ {
				if dp[i-1][j][k] < 0 {
					continue
				}

				curr := dp[i-1][j][k]
				for d := 0; d < len(dirs); d++ {
					x0, y0 := j+dirs[d][0], k+dirs[d][1]

					if x0 < 0 || x0 >= w || y0 < 0 || y0 >= w {
						continue
					}

					if x0 == y0 {
						dp[i][x0][y0] = max(dp[i][x0][y0], curr+grid[i][x0])
					} else {
						dp[i][x0][y0] = max(dp[i][x0][y0], curr+grid[i][x0]+grid[i][y0])
					}
				}
			}
		}
	}

	var ans int

	for i := range dp[h-1] {
		for j := i; j < w; j++ {
			if dp[h-1][i][j] > ans {
				ans = dp[h-1][i][j]
			}
		}
	}

	return ans
}

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
