package challenges

func maximalRectangle(matrix [][]byte) int {
	if matrix == nil || len(matrix) == 0 {
		return 0
	}

	h, w := len(matrix), len(matrix[0])

	if w == 0 {
		return 0
	}

	if h == 1 && w == 1 {
		if matrix[0][0] == '0' {
			return 0
		}

		return 1
	}

	var ans, area int
	var hist []int

	for i := 0; i < h; i++ {
		updated := false
		next := make([]int, w)

		for j := 0; j < w; j++ {
			if i == 0 {
				if matrix[i][j] == '1' {
					next[j]++
				}

				continue
			}

			if matrix[i][j] == '1' {
				next[j] = hist[j] + 1
			} else {
				next[j] = 0
				if hist == nil || hist[j] != 0 {
					updated = true
				}
			}
		}

		if updated && hist != nil {
			area = calcRect(hist)
			if area > ans {
				ans = area
			}
		}

		// fmt.Println(i, next, area)

		hist = next
	}

	area = calcRect(hist)
	if area > ans {
		ans = area
	}

	return ans
}

func calcRect(heights []int) int {
	n := len(heights)
	stack := make([][]int, 0, n)

	var ans, area int

	for i, h := range heights {
		if h == 0 {
			// if 0, empty and update
			for _, unit := range stack {
				area = (unit[0] * (i - unit[1]))

				if area > ans {
					ans = area
				}
			}

			stack = stack[:0]
			continue
		}

		last := len(stack) - 1

		// taller, append to the tail
		if last < 0 || h > stack[last][0] {
			stack = append(stack, []int{h, i})
			continue
		}

		// same height, continue
		if h == stack[last][0] {
			continue
		}

		// lower than previous towers
		j := last
		start := i

		for j >= 0 {
			if stack[j][0] <= h {
				break
			}

			if stack[j][1] < start {
				start = stack[j][1]
			}

			area = stack[j][0] * (i - stack[j][1])
			if area > ans {
				ans = area
			}

			j--
		}

		stack = stack[:j+1]

		if j < 0 || stack[j][0] < h {
			stack = append(stack, []int{h, start})
		}
	}

	if len(stack) > 0 {
		for _, unit := range stack {
			area = (unit[0] * (n - unit[1]))

			if area > ans {
				ans = area
			}
		}
	}

	return ans
}
