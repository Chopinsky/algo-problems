package challenges

/**
=============
Problem:
Array of numbers, all but two will appear twice, and these two only appear once.

Solution:
XOR will cancel numbers appearing twice.
*/
func singleNumberIII(arr []int) []int {
	bits := 0

	// all but `a` and `b` will be cancelled out, and
	// eventually, `bits = a ^ b`
	for _, val := range arr {
		bits ^= val
	}

	// idea is that for the lowest bits that equals 1, either `a`
	// or `b` (not both, not neither) has 1 at this position. So
	// we repeat the XOR accumulations, but this time, `flip` = a
	lowestBit := bits & -bits
	flip := 0

	for _, val := range arr {
		if val & lowestBit > 0 {
			flip ^= val
		}
	}

	// bits = a ^ b; flip = a; then bits ^ flip = (a ^ b) ^ a = b
	// flip ^ bits
	return []int{flip, flip ^ bits}
}
