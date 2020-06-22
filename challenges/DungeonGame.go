package challenges

func calculateMinimumHP(d [][]int) int {
	if d == nil || len(d) == 0 {
		return 1
	}

	h, w := len(d), len(d[0])
	dp := make([][]int, h)

	for i := range dp {
		dp[i] = make([]int, w)
	}

	if d[h-1][w-1] >= 0 {
		dp[h-1][w-1] = 1
	} else {
		dp[h-1][w-1] = 1 - d[h-1][w-1]
	}

	t := h + w - 3
	for t >= 0 {
		i, j := t, 0
		if i >= h {
			i = h - 1
			j = t - i
		}

		for i >= 0 && j < w {
			if i+1 >= h {
				dp[i][j] = hp(dp[i][j+1], d[i][j])
			} else if j+1 >= w {
				dp[i][j] = hp(dp[i+1][j], d[i][j])
			} else {
				v0 := hp(dp[i][j+1], d[i][j])
				v1 := hp(dp[i+1][j], d[i][j])

				if v0 < v1 {
					dp[i][j] = v0
				} else {
					dp[i][j] = v1
				}
			}

			i--
			j++
		}

		t--
	}

	if dp[0][0] == 0 {
		return 1
	}

	return dp[0][0]
}

func hp(last, val int) int {
	if last == 0 {
		if val > 0 {
			return 0
		}

		return 1 - val
	}

	h := last - val
	if h < 0 {
		return 0
	}

	return h
}
