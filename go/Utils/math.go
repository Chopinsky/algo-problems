package utils

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

const (
	// MaxUint ...
	MaxUint = ^uint(0)

	// MaxInt ...
	MaxInt = int(MaxUint >> 1)
)

// Epsilon ...
var Epsilon = math.Nextafter(1.0, 2.0) - 1.0

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

// Sqrt ...
func Sqrt(num int) float64 {
	if num < 0 {
		return -1.
	}

	if num == 0 {
		return 0.
	}

	x := float64(num)
	y := x
	delta, temp := 1., 0.

	for delta >= Epsilon {
		temp = 0.5 * (y + x/y)
		delta = math.Abs(temp - y)
		y = temp
	}

	return y
}

// GreatestCommonDenominator ...
func GreatestCommonDenominator(a, b int) int {
	if a == 0 || b == 0 {
		return 0
	}

	if a == b {
		return a
	}

	if a > b {
		a, b = b, a
	}

	var t int
	for t > 0 {
		t = b % a
		a, b = t, a
	}

	return b
}

// LeastCommonMultiple ...
func LeastCommonMultiple(a, b int) int {
	return (a * b) / GreatestCommonDenominator(a, b)
}

// RandIntArr ...
func RandIntArr(m, n int) []int {
	if m > n {
		return []int{}
	}

	rand.Seed(time.Now().UnixNano() / 42)
	result := make([]int, 0, m)

	for i := 0; i < n; i++ {
		if rand.Int()%(n-i) < m {
			result = append(result, i)
			if len(result) == m {
				break
			}

			m--
		}
	}

	return result
}

// ComplementNumber ...
func ComplementNumber(num int) int {
	var base uint
	var comp int

	for num > 0 {
		// flip last bit to 1 if 0, and to 0 if 1
		bit := 1 - num&1

		// add to the complement number
		if base > 0 {
			comp += bit << base
		} else {
			comp = bit
		}

		// update states
		num = num >> 1
		base++
	}

	return comp
}
