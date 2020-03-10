package shared

import "fmt"

// DEBUG ...
var DEBUG = false

// Dirs ...
var Dirs = []int{-1, 0, 1, 0, -1}

// Problem ...
type Problem interface {
	Solve()
}

// Print ...
func Print(num int, res, calc interface{}) {
	fmt.Println("\n >> Solving Problem #", num+1, "<<")
	fmt.Println("Caculation: ", calc)
	fmt.Println("Expecting:  ", res)
	fmt.Println()
}

// SetDebug ...
func SetDebug(val bool) {
	DEBUG = val
}

// DebugMode ...
func DebugMode() bool {
	return DEBUG
}

// GenerateBinarySet ...
func GenerateBinarySet(start int, length uint) []int {
	result := []int{start, 0, 1 << length}
	val := start

	for val > 0 {
		val = (val - 1) & start
		result = append(result, val)
	}

	return result
}

// BinaryGCD ...
func BinaryGCD(a, b int) (int, int) {
	d := 0

	for a%2 == 0 && b%2 == 0 {
		a /= 2
		b /= 2
		d++
	}

	for a != b {
		if a%2 == 0 {
			a /= 2
		} else if b%2 == 0 {
			b /= 2
		} else if a > b {
			a = (a - b) / 2
		} else {
			b = (b - a) / 2
		}
	}

	return a, d
}

// GCD ...
func GCD(a, b int) int {
	if a == b {
		return a
	}

	if a < b {
		a, b = b, a
	}

	for b != 0 {
		a = a % b
		a, b = b, a
	}

	return a
}
