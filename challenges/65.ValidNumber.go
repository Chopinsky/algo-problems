package challenges

import (
	"fmt"
	"strings"
)

func isNumber(s string) bool {
	s = strings.Trim(s, " \t")

	size := len(s)
	if size == 0 {
		return false
	}

	ePos := -1
	dotPos := -1

	for i, ch := range s {
		if ch != '+' && ch != '-' && ch != 'e' && ch != '.' && (ch > '9' || ch < '0') {
			return false
		}

		if i == 0 && ch == 'e' {
			return false
		}

		if ch == '+' || ch == '-' {
			// if having the + or - sign other than the 1st char in the
			// string, or the 1st char behind e, it's not valid
			if i != 0 && ((ePos < 0) || (i-ePos != 1)) {
				return false
			}

			continue
		}

		if ch == 'e' {
			if ePos > 0 || i == size-1 {
				// don't allow 2 `e` characters, or the last char in the string
				return false
			}

			ePos = i
			continue
		}

		if ch == '.' {
			if ePos > 0 || dotPos >= 0 {
				return false
			}

			dotPos = i
			continue
		}
	}

	// todo: do the number validations
	var l, r string

	if ePos > 0 {
		l = s[:ePos]
		r = s[ePos+1:]
	} else {
		l = s
	}

	if l != "" && (l[0] == '+' || l[0] == '-') {
		if len(l) == 1 {
			return false
		}

		l = l[1:]
		dotPos--
	}

	if r != "" && (r[0] == '+' || r[0] == '-') {
		if len(r) == 1 {
			return false
		}
	}

	fmt.Println(l, dotPos, ePos)

	if dotPos >= 0 && len(l) == 1 {
		return false
	}

	return true
}
