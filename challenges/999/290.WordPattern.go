package challenges

import "strings"

func wordPattern(pattern string, str string) bool {
	if str == "" || pattern == "" {
		return false
	}

	s := strings.Split(str, " ")
	if len(pattern) != len(s) {
		return false
	}

	pmap := make(map[byte]string)
	rmap := make(map[string]bool)

	for i, char := range pattern {
		// fmt.Println(char, s[i])

		if word, ok := pmap[byte(char)]; ok {
			if word != s[i] {
				return false
			}
		} else {
			if rmap[s[i]] {
				return false
			}

			pmap[byte(char)] = s[i]
			rmap[s[i]] = true
		}
	}

	return true
}
