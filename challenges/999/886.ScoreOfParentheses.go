package challenges

func scoreOfParentheses(s string) int {
	stack := make([]int, 0, 50)
	var ans int

	for _, ch := range s {
		if ch == '(' {
			stack = append(stack, 0)
		} else {
			size := len(stack)
			val := stack[size-1]

			if val == 0 {
				val = 1
			}

			if size > 1 {
				stack[size-2] += 2 * val
			} else {
				ans += val
			}

			stack = stack[:size-1]
		}
	}

	return ans
}
