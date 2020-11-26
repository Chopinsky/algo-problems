package challenges

import (
	// "fmt"
	"math"
)

func preimageSizeFZF(k int) int {
	if k <= 4 {
		return 5
	}

	l, r := getRange(k)
	cl, cr := tz(l), tz(r)

	// fmt.Println(l, r, cl, cr)

	if k > cr {
		return 0
	}

	if k == cl || k == cr {
		return 5
	}

	var m, count int

	for l < r {
		m = (l + r) / 2
		count = tz(m)

		// fmt.Println(l, r, m, count)

		if count == k {
			return 5
		}

		if count > k {
			r = m - 1
		} else {
			l = m + 1
		}
	}

	count = tz(l)
	if count == k {
		return 5
	}

	return 0
}

func tz(n int) int {
	count := n

	for n >= 5 {
		count += n / 5
		n /= 5
	}

	return count
}

func getRange(k int) (int, int) {
	n := int(math.Floor(math.Log(4*float64(k)+1) / math.Log(5.0)))

	base, i := 5, 1

	for i < n-1 {
		base *= 5
		i++
	}

	// fmt.Println("base:", n, base)

	return base, 5*base - 1
}
