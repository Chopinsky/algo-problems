package challenges

func rotate(nums []int, k int) {
	length := len(nums)
	if length < 2 {
		return
	}

	k = k % length
	if k == 0 {
		return
	}

	reverseRotate(nums, length-k, length-1)
	reverseRotate(nums, 0, length-k-1)
	reverseRotate(nums, 0, length-1)
}

func reverseRotate(nums []int, start int, end int) {
	count := (end - start + 1) / 2

	for i := 0; i < count; i++ {
		src := i + start
		tgt := end - i
		nums[src], nums[tgt] = nums[tgt], nums[src]
	}
}
