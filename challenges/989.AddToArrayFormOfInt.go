package challenges

func addToArrayForm(a []int, k int) []int {
	if k == 0 {
		return a
	}

	reverse(a, len(a))
	var rem, val, one, i int

	for {
		rem = k % 10
		k /= 10

		if i >= len(a) {
			val = rem + one
			a = append(a, 0)
		} else {
			val = a[i] + rem + one
		}

		if val >= 10 {
			a[i] = val - 10
			one = 1
		} else {
			a[i] = val
			one = 0
		}

		if k == 0 && one == 0 {
			break
		}

		i++
	}

	if one == 1 {
		a = append(a, 1)
	}

	reverse(a, len(a))
	return a
}

func reverse(a []int, size int) {
	for i := 0; i < size/2; i++ {
		a[i], a[size-i-1] = a[size-i-1], a[i]
	}
}
