package challenges

func largestRectangleArea(heights []int) int {
	if heights == nil || len(heights) == 0 {
		return 0
	}

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
