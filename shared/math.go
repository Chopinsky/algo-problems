package shared

import "fmt"

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

// GCDUint64 ...
func GCDUint64(a, b uint64) uint64 {
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

// FastPower ...package shared
func FastPower(a, b, n, mod uint64) uint64 {
	if a == 0 {
		a = 1
	}

	if mod < 1 {
		mod = 1
	}

	for n > 0 {
		if n&1 == 1 {
			a *= b % mod
		}

		b = b * b % mod
		n = n >> 1
	}

	return a
}

// MtrxMulti ...
func MtrxMulti(a, b [][]uint64, mod uint64) [][]uint64 {
	if a == nil || b == nil {
		fmt.Println("null matrices provided ... ")
		return nil
	}

	h, w, hb := len(a), len(a[0]), len(b)

	if w != hb {
		fmt.Println("mismatched matrix demensions ... ")
		return nil
	}

	if mod < 1 {
		mod = 1
	}

	result := make([][]uint64, h)
	for i := 0; i < h; i++ {
		result[i] = make([]uint64, w)
	}

	// actual multiplications
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			for k := 0; k < w; k++ {
				result[i][j] += a[i][k] * b[k][j] % mod
			}
		}
	}

	return result
}
