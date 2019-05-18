package utils

import "fmt"

const (
	// MaxUint ...
	MaxUint = ^uint(0)

	// MaxInt ...
	MaxInt = int(MaxUint >> 1)
)

// Min ...
func Min(a, b int) int {
	if a > b {
		return b
	}

	return a
}

// Max ...
func Max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

// BinarySearch ...
func BinarySearch(src []int, target int) (int, bool) {
	l := 0
	u := len(src) - 1

	for l <= u {
		m := (l + u) / 2
		if src[m] < target {
			l = m + 1
		} else if src[m] == target {
			return m, true
		} else {
			u = m - 1
		}

		Debug(fmt.Sprintln("New bounds: ", l, u), 0)
	}

	if u >= 0 || l >= len(src) {
		return u, false
	}

	return l, false
}
