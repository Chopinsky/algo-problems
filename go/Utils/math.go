package utils

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
