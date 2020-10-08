package challenges

func binarySearch(nums []int, target int) int {
	size := len(nums)
	if size == 0 {
		return -1
	}

	if size == 1 {
		if nums[0] == target {
			return 0
		}

		return -1
	}

	if target < nums[0] || target > nums[size-1] {
		return -1
	}

	l, r := 0, size

	for l < r {
		m := (l + r) / 2
		if nums[m] == target {
			return m
		}

		if nums[m] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}

	if nums[l] == target {
		return l
	}

	return -1
}
