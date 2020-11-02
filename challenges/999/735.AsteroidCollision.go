package challenges

func asteroidCollision(a []int) []int {
	size := len(a)
	ans := make([]int, 0, size)

	for i := range a {
		ans = append(ans, a[i])

		i := len(ans) - 1
		for i >= 1 {
			if ans[i] == 0 {
				ans = ans[:i]
				break
			}

			if ans[i-1] < 0 || ans[i] > 0 {
				break
			}

			if ans[i-1] == -ans[i] {
				ans = ans[:i-1]
				i--
			} else if ans[i-1] > -ans[i] {
				ans = ans[:i]
				break
			} else {
				ans[i-1] = ans[i]
				ans = ans[:i]
			}

			i--
		}
	}

	return ans
}
