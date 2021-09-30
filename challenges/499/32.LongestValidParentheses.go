package challenges

/**
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0
*/

// the idea is to use stacks to store the left-parenthese, and pop
// on every right-parenthese, and count / merge / extend the valid
// range
func longestValidParentheses(s string) int {
	if len(s) < 2 {
		return 0
	}

	stack := make([]int, 0, len(s))
	stack = append(stack, -1)
	var long int

	for i, val := range s {
		if val == '(' {
			stack = append(stack, i)
			continue
		}

		// pop last, last will always be -1 before empty,
		// meaning we're reaching the 1st illegal ')'
		stack = stack[:len(stack)-1]

		if len(stack) == 0 {
			// if empty, meaning all prvious valid substrings have
			// been exhuasted
			stack = append(stack, i)
		} else {
			// valid, we can check the length since the last valid
			// ends
			l := i - stack[len(stack)-1]

			if l > long {
				long = l
			}
		}
	}

	return long
}

func longestValidParentheses1(s string) int {
	if len(s) < 2 {
		return 0
	}

	stack := make([]int, 0, len(s))
	rng := make([][]int, 0, len(s))

	var long, front int

	for i, val := range s {
		if val == '(' {
			stack = append(stack, i)
		} else {
			if len(stack) == 0 {
				continue
			}

			last := len(stack) - 1
			front, stack = stack[last], stack[:last]

			if len(rng) == 0 {
				if i == front+1 {
					rng = append(rng, []int{front, i})
					if long < 2 {
						long = 2
					}
				}

				continue
			}

			valid := false
			if i == front+1 {
				valid = true
			}

			for len(rng) > 0 {
				last := rng[len(rng)-1]

				// expand valid
				if last[1]+1 == front {
					rng = rng[:len(rng)-1]
					front = last[0]
					valid = true
					break
				}

				// last range included
				if last[0] != front+1 || last[1] != i-1 {
					break
				}

				rng = rng[:len(rng)-1]
				valid = true
			}

			if valid {
				if i-front+1 > long {
					long = i - front + 1
				}

				rng = append(rng, []int{front, i})
			}

			// fmt.Println(front, i, valid, stack, rng)

			if i == len(s)-1 {
				if front >= 0 && i > front && i-front+1 > long {
					long = i - front + 1
				}
			}
		}
	}

	return long
}
