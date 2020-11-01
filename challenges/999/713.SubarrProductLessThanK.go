package challenges

func numSubarrayProductLessThanK(nums []int, k int) int {
	if k <= 1 {
		return 0
	}

	size := len(nums)
	prod := nums[0]

	var l, r, ans int

	for l < size {
		// fmt.Println("mv l", l, r, ans, prod)

		if prod < k {
			ans += r - l + 1
		}

		// move right boundary & count
		for prod < k && r+1 < size {
			if prod*nums[r+1] >= k {
				break
			}

			r++
			ans++
			prod *= nums[r]
		}

		// move left boundary & count
		prod /= nums[l]
		l++

		if r < l && l < size {
			r = l
			prod = nums[l]
		}
	}

	return ans
}
