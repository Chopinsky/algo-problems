package challenges

func firstMissingPositive(nums []int) int {
	for i := range nums {
		shuffle(nums, i)
	}

	// fmt.Println(nums)

	for i, val := range nums {
		if i+1 != val {
			return i + 1
		}
	}

	return len(nums) + 1
}

func shuffle(nums []int, idx int) {
	val := nums[idx]

	if val <= 0 || val-1 >= len(nums) || nums[val-1] == val {
		return
	}

	nums[val-1], nums[idx] = val, nums[val-1]

	shuffle(nums, idx)
}
