package challenges

// import "fmt"

/**
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.

Example 1:

Input: password = "a"
Output: 5

Example 2:

Input: password = "aA1"
Output: 3

Example 3:

Input: password = "1337C0d3"
Output: 0

Constraints:

1 <= password.length <= 50
password consists of letters, digits, dot '.' or exclamation mark '!'.
*/

func strongPasswordChecker0(s string) int {
	var ans, i int

	a, A, d := 1, 1, 1
	size := len(s)
	repeat := make([]int, size)

	for i < size {
		switch charType(s[i]) {
		case 0:
			a = 0

		case 1:
			A = 0

		case 2:
			d = 0
		}

		start := i
		for i < size && s[i] == s[start] {
			i++
		}

		repeat[start] = i - start
	}

	missing := a + A + d
	// fmt.Println(missing, repeat)

	if size < 6 {
		return missing + max(0, 6-size-missing)
	}

	del := max(size-20, 0)
	left := 0
	ans += del

	for k := 1; k < 3; k++ {
		for i := 0; i < size && del > 0; i++ {
			// no need for deletion actions
			if repeat[i] < 3 || repeat[i]%3 != (k-1) {
				continue
			}

			// make a deletion of k-characters from the repeating char
			// substring
			repeat[i] -= min(del, k)
			del -= k
		}
	}

	for i := 0; i < size; i++ {
		// delete any extra chars in the repeating space
		if repeat[i] >= 3 && del > 0 {
			more := repeat[i] - 2
			repeat[i] -= del
			del -= more
		}

		// if there are more than 3 repeating chars left,
		if repeat[i] >= 3 {
			left += repeat[i] / 3
		}
	}

	return ans + max(missing, left)
}

func strongPasswordChecker(s string) int {
	if len(s) <= 4 {
		return 6 - len(s)
	}

	missing, pivots, ones, twos := check(s)
	// fmt.Println( missing, pivots, ones, twos)

	if len(s) < 6 {
		return max(missing, 6-len(s))
	}

	if len(s) <= 20 {
		return max(missing, pivots)
	}

	del := len(s) - 20

	pivots -= min(del, ones)
	pivots -= min(max(del-ones, 0), twos*2) / 2
	pivots -= max(del-ones-2*twos, 0) / 3

	return del + max(missing, pivots)
}

func check(s string) (int, int, int, int) {
	found := make([]bool, 3)

	for _, c := range s {
		t := charType(byte(c))
		if t < 0 {
			continue
		}

		found[t] = true
	}

	i, size := 2, len(s)
	var pivots, ones, twos, runningLen int

	for i < size {
		if runningLen > 0 {
			// we're in the running mode, check what to do
			if s[i] != s[i-1] {
				// fmt.Println("breaking:", runningLen)

				// number of pivot running segments that we shall break: either do
				// a change to a char of a missing type, or delete it
				pivots += runningLen / 3

				// number of sequences where we shall delete 1 char and call it good when
				// all other requirements are met
				if runningLen%3 == 0 {
					ones++
				}

				// number of sequences where we shall delete 2 chars and call it good when
				// all other requirements are met
				if runningLen%3 == 1 {
					twos++
				}

				// a different char, reset the mode, and process what we got so far
				runningLen = 0
			} else {
				// running mode continues, update the length of the current running
				// sequence
				runningLen++
			}
		} else if s[i] == s[i-1] && s[i] == s[i-2] {
			// start the running mode
			runningLen = 3
		}

		i++
	}

	if runningLen > 0 {
		pivots += runningLen / 3

		if runningLen%3 == 0 {
			ones++
		}

		if runningLen%3 == 1 {
			twos++
		}
	}

	missing := 0
	for _, val := range found {
		if !val {
			missing++
		}
	}

	return missing, pivots, ones, twos
}

func charType(char byte) int {
	if char <= 'z' && char >= 'a' {
		return 0
	}

	if char <= 'Z' && char >= 'A' {
		return 1
	}

	if char <= '9' && char >= '0' {
		return 2
	}

	return -1
}
