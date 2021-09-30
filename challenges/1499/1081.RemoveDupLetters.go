package challenges

func removeDuplicateLetters(s string) string {
	stack := make([]rune, 0, len(s))
	last := make([]int, 26)

	for i, ch := range s {
		last[int(ch-'a')] = i
	}

	seen := make([]int, 26)
	var idx, jdx, top int

	for i, ch := range s {
		idx = int(ch - 'a')
		seen[idx]++

		// see the element for the first time in the stack
		if seen[idx] > 1 {
			continue
		}

		// pop anything that can be found later, but is larger than
		// the current char
		for len(stack) > 0 {
			top = len(stack) - 1
			jdx = int(stack[top] - 'a')

			// check if the top char can be popped
			if stack[top] < ch || (stack[top] != ch && i > last[jdx]) {
				break
			}

			// pop and reset
			seen[jdx] = 0
			stack = stack[:top]
		}

		// fmt.Println(i, ch, stack)

		stack = append(stack, ch)
	}

	// fmt.Println(stack, last)

	return string(stack)
}
