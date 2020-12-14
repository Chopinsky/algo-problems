package challenges

import "strings"

func partition(s string) [][]string {
	ans := make([][]string, 0, len(s))
	splitStr(make([]string, 0, len(s)), s, &ans)

	return ans
}

func splitStr(curr []string, s string, ans *[][]string) {
	l := len(strings.Join(curr, ""))

	// recursion at the end of the string
	if l == len(s) {
		next := make([]string, len(curr))
		copy(next, curr)
		*ans = append(*ans, next)

		return
	}

	for r := l; r < len(s); r++ {
		if !isPali(s, l, r) {
			continue
		}

		splitStr(append(curr, s[l:r+1]), s, ans)
	}

	return
}

func partition1(s string) [][]string {
	cache := make(map[string][][]string)
	ans := split(s, cache)

	for i := 0; i < len(ans); i++ {
		l := len(ans[i])
		for j := 0; j < l/2; j++ {
			ans[i][j], ans[i][l-1-j] = ans[i][l-1-j], ans[i][j]
		}
	}

	return ans
}

func split(s string, cache map[string][][]string) [][]string {
	if len(s) == 0 {
		return nil
	}

	if arr, ok := cache[s]; ok {
		return arr
	}

	ans := make([][]string, 0, len(s))

	for i := len(s) - 1; i >= 0; i-- {
		if !isPali(s, 0, i) {
			continue
		}

		arr := split(s[i+1:], cache)

		if len(arr) > 0 {
			for _, str := range arr {
				next := make([]string, len(str))
				copy(next, str)
				next = append(next, s[:i+1])
				ans = append(ans, next)

				// if s == "aabbbccc" {
				//   fmt.Println(s[:i+1], str, ans)
				// }
			}
		} else {
			ans = append(ans, []string{s[:i+1]})
		}
	}

	// fmt.Println("cache:", s, ans)

	cache[s] = ans

	return ans
}

func isPali(s string, i, j int) bool {
	if i >= j {
		return i == j
	}

	m := (j - i + 1) / 2
	for o := 0; o < m; o++ {
		if s[i+o] != s[j-o] {
			return false
		}
	}

	return true
}
