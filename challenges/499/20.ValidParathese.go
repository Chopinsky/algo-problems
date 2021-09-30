package challenges

/**
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
*/

func isValidString(s string) bool {
	stack := make([]byte, 0, len(s))

	for _, c := range s {
		if c == '(' || c == '[' || c == '{' {
			stack = append(stack, byte(c))
			continue
		}

		top := len(stack) - 1
		if top < 0 {
			return false
		}

		if (c == ')' && stack[top] != '(') || (c == ']' && stack[top] != '[') || (c == '}' && stack[top] != '{') {
			return false
		}

		stack = stack[:top]
	}

	return len(stack) == 0
}
