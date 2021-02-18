package challenges

/**
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]

Example 3:

Input: S = "12345"
Output: ["12345"]

Example 4:

Input: S = "0"
Output: ["0"]

Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
*/

var diff = byte('a') - byte('A')

func letterCasePermutation(S string) []string {
	ans := make(map[string]bool, len(S)*len(S))
	perm([]byte(S), ans, 0)

	ret := make([]string, 0, len(ans))
	for k := range ans {
		ret = append(ret, k)
	}

	return ret
}

func perm(s []byte, ans map[string]bool, idx int) {
	curr := string(s)
	if !ans[curr] {
		ans[curr] = true
	}

	for idx < len(s) && s[idx] <= byte('9') && s[idx] >= byte('0') {
		idx++
	}

	if idx >= len(s) {
		return
	}

	if idx+1 < len(s) {
		perm(s, ans, idx+1)
	}

	if s[idx] <= byte('z') && s[idx] >= byte('a') {
		s[idx] -= diff

		// fmt.Println(s)

		next := string(s)
		if !ans[next] {
			ans[next] = true
		}

		if idx+1 < len(s) {
			perm(s, ans, idx+1)
		}

		s[idx] += diff
	} else {
		s[idx] += diff

		// fmt.Println(s)

		next := string(s)
		if !ans[next] {
			ans[next] = true
		}

		if idx+1 < len(s) {
			perm(s, ans, idx+1)
		}

		s[idx] -= diff
	}
}
