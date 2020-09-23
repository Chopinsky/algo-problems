package challenges

import "sort"

func sequentialDigits(low int, high int) []int {
	_, count := breakdown(low)
	ans := make([]int, 0, 200)

	for i := 1; i < 10; i++ {
		ans = genNumbers(i, count, low, high, ans)
	}

	sort.Ints(ans)

	return ans
}

func breakdown(val int) (int, int) {
	base := 0
	count := 0

	for val > 0 {
		if val < 10 {
			base = val
		}

		count++
		val /= 10
	}

	return base, count
}

func genNumbers(base, count, low, high int, ans []int) []int {
	if base+count > 10 {
		return ans
	}

	sum := 0
	for base < 10 {
		sum = sum*10 + base
		base++

		if sum >= low && sum <= high {
			ans = append(ans, sum)
		}

		if sum > high {
			break
		}
	}

	return ans
}
