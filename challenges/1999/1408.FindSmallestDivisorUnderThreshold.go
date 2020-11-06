package challenges

func smallestDivisor(nums []int, threshold int) int {
	size := len(nums)
	if size == 1 {
		return div(nums[0], threshold)
	}

	sort.Ints(nums)

	if threshold == size {
		return nums[size-1]
	}

	l, r := 1, nums[size-1]
	best := r

	for l < r {
		m := (l + r) / 2
		v := sum(nums, m)

		// fmt.Println(m, l, r, v, threshold)

		if v <= threshold {
			if m < best {
				best = m
			}

			r = m - 1
		} else {
			l = m + 1
		}
	}

	if sum(nums, l) > threshold {
		return best
	}

	return l
}

func sum(nums []int, base int) int {
	s := 0

	for _, v := range nums {
		if v <= base {
			s++
			continue
		}

		s += div(v, base)
	}

	return s
}

func div(a, b int) int {
	if a%b == 0 {
		return a / b
	}

	return (a / b) + 1
}
