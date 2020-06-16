package main

// BinarySearch ...
func BinarySearch(src []int, l, r, val int) int {
	if val < src[l] {
		return l
	}

	if val >= src[r] {
		return r + 1
	}

	var m int
	for l <= r {
		m = (l + r) / 2
		if val < src[m] {
			r = m - 1
		} else if val >= src[m] {
			l = m + 1
		}
	}

	return l
}

// InsertSort ...
func InsertSort(src []int, l, r int) {
	if r-l < 1 {
		return
	}

	var j, temp int

	for i := l + 1; i <= r; i++ {
		j = i - 1
		temp = src[i]

		for j >= l && temp < src[j] {
			src[j+1] = src[j]
			j--
		}

		src[j+1] = temp
	}
}
