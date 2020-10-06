package challenges

import (
	"fmt"
	"math"
)

func runSGB() {
	fmt.Println(smallestGoodBase("13"), "3")
	fmt.Println(smallestGoodBase("4681"), "8")
	fmt.Println(smallestGoodBase("1000000000000000000"), "999999999999999999")
}

func smallestGoodBase(n string) string {
	var base uint64

	for _, v := range n {
		num := uint64(v - '0')
		base = base*10 + num
	}

	if base == 3 {
		return "2"
	}

	fmt.Println(base)

	start := int(math.Log2(float64(base+1))) + 1

	for i := start; i > 1; i-- {
		val := findBase(base, i)

		// fmt.Println(i, val)

		if val > 0 {
			return stringify(val)
		}
	}

	return stringify(base - 1)
}

func findBase(num uint64, f int) uint64 {
	l := 2
	r := int(math.Pow(float64(num+1), 1.0/float64(f)))

	// fmt.Println("before:", l, r, f)

	for l <= r {
		m := (l + r) / 2

		base := 1
		sum := 0

		for i := 0; i <= f; i++ {
			sum += base
			base *= m
		}

		// fmt.Println("sum:", sum, m, f)

		if uint64(sum) == num {
			return uint64(m)
		}

		if uint64(sum) < num {
			l = m + 1
		} else {
			r = m - 1
		}
	}

	return 0
}

func stringify(val uint64) string {
	base := make([]byte, 0, 18)

	for val > 0 {
		base = append(base, '0'+byte(val%10))
		val /= 10
	}

	size := len(base)
	for i := 0; i < size/2; i++ {
		base[i], base[size-i-1] = base[size-i-1], base[i]
	}

	return string(base)
}
