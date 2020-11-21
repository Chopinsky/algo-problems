package challenges

/**
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
*/
func search2(nums []int, target int) bool {
	if nums == nil || len(nums) == 0 {
		return false
	}

	size := len(nums)
	if size == 1 {
		return target == nums[0]
	}

	if nums[0] < nums[size-1] {
		return bSearch(nums, target)
	}

	p, found := findPeak(nums, target, size)

	// fmt.Println(p, found)

	if found {
		return true
	}

	if p >= size-1 {
		return bSearch(nums, target)
	}

	if target > nums[p] || target < nums[p+1] {
		return false
	}

	if target < nums[0] {
		return bSearch(nums[p+1:], target)
	}

	return bSearch(nums[:p+1], target)
}

func findPeak(nums []int, target, size int) (int, bool) {
	l, r := 0, size

	for l < r {
		m := (l + r) / 2
		if target == nums[m] {
			return -1, true
		}

		trend, peak := findTrend(nums, m, l, r)

		// fmt.Println("mid", l, m, r, trend, peak)

		// nums[l] == nums[m] == nums[r], should have been caught already
		if peak >= 0 {
			return peak, false
		}

		if trend > 0 {
			l = m + 1
		} else {
			r = m - 1
		}
	}

	return l, false
}

func findTrend(nums []int, m, l, r int) (int, int) {
	rr, ll := m+1, m-1
	last := len(nums) - 1
	base := nums[m]

	for rr < r && rr < last && nums[rr] == nums[rr-1] {
		rr++
	}

	for ll > l && ll > 0 && nums[ll] == nums[ll+1] {
		ll--
	}

	if ll < 0 {
		if nums[m] < nums[rr] {
			return 1, -1
		}

		return -1, -1
	}

	if rr > last {
		if nums[m] < nums[ll] {
			return -1, -1
		}

		return 1, -1
	}

	if base >= nums[ll] && base > nums[rr] {
		// fmt.Println(":top", ll, m, rr)
		return 0, rr - 1
	}

	if nums[ll] >= nums[l] && base < nums[l] {
		// fmt.Println(":dip", ll, m, rr)
		return 0, ll
	}

	if nums[ll] <= base && base <= nums[rr] {
		// fmt.Println(":rising", ll, m, rr)
		if base < nums[l] || (base == nums[l] && nums[rr] == nums[l]) {
			return -1, -1
		}

		return 1, -1
	}

	var right int
	if r > last {
		right = nums[r-1]
	} else {
		right = nums[r]
	}

	// fmt.Println(":falling", ll, m, rr, base, right)

	if base > right || (base == right && nums[ll] == right) {
		return 1, -1
	}

	return -1, -1
}

func bSearch(nums []int, target int) bool {
	if target < nums[0] || target > nums[len(nums)-1] {
		return false
	}

	l, r := 0, len(nums)
	for l < r {
		m := (l + r) / 2

		if nums[m] == target {
			return true
		}

		if nums[m] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}

	return nums[l] == target
}
