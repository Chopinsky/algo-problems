package challenges

func findDuplicates(nums []int) []int {
	res := make([]int, 0, len(nums))

	for i := range nums {
		idx := abs(nums[i]) - 1
		if nums[idx] < 0 {
			res = append(res, idx+1)
		} else {
			nums[idx] = -1 * nums[idx]
		}
	}

	// fmt.Println(nums)

	return res
}

func abs(num int) int {
	if num < 0 {
		return -1 * num
	}

	return num
}

func findDuplicates1(nums []int) []int {
	marker := make([]int, len(nums))
	res := make([]int, 0, len(nums))

	for i := range nums {
		if marker[nums[i]-1] > 0 {
			res = append(res, nums[i])
			continue
		}

		marker[nums[i]-1]++
	}

	return res
}
