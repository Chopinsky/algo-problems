package challenges

import (
	"fmt"
	"math"
)

func distributeCandies(candies int, numPpl int) []int {
	k := getK(candies, numPpl)
	res := make([]int, numPpl)

	fmt.Println(k)

	for i := range res {
		if k < 0 {
			if candies >= i+1 {
				res[i] = i + 1
				candies -= res[i]
			} else {
				res[i] = candies
				candies -= res[i]
				break
			}
		} else {
			res[i] = (k+1)*(i+1) + k*(k+1)*numPpl/2
			candies -= res[i]
		}
	}

	fmt.Println(res, candies)

	if candies > 0 {
		for i := range res {
			extra := (k+1)*numPpl + i + 1

			if candies <= extra {
				// fmt.Println("last", candies)
				res[i] += candies
				break
			}

			// fmt.Println("extra", (k + 1) * numPpl + i + 1)
			res[i] += extra
			candies -= extra
		}
	}

	return res
}

func getK(num, n int) int {
	base := n * (n + 1) / 2
	if base >= num {
		return -1
	}

	if 2*base+n*n >= num {
		return 0
	}

	a := float64(n * n)
	b := float64(base) + a/2
	c := 2 * a * float64(num-base)

	k := int((math.Sqrt(b*b+c) - b) / a)
	return k
}
