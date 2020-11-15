package challenges

func find132pattern(nums []int) bool {
	if nums == nil || len(nums) < 3 {
		return false
	}

	// stack is the mono-decreasing stack, which stores larger
	// numbers to the right of the current cursor
	stack := make([]int, 0, len(nums))

	// this will be the index for the number of index j of
	// the "i-j-k" in the "1-3-2" pattern
	topSmall := -1

	for i := len(nums) - 1; i >= 0; i-- {
		n := nums[i]

		// if there's ever a number popped out, meaning we have the
		// "32" pattern somewhere already, check the "13" part and we're
		// done: here, "3" can be any number that's in the stack, and
		// topSmall is the largest number that's smaller than any number
		// the stack; the popping mechanism always guarantee we have some
		// number in the stack
		if topSmall >= 0 && n < nums[topSmall] {
			return true
		}

		// pop from the stack: get rid of all the numbers to the
		// right of the cursor but is smaller than the current
		// number under the cursor, such that it warrents the
		// 132 pattern if we can get it.
		last := len(stack) - 1
		for last >= 0 && n > nums[stack[last]] {
			last--
		}

		// n <= nums[stack[last]], we pop anything to the right of the
		// last index, and if there is such a number, it will be the
		// largest number that's smaller than the current number (maybe
		// the "3") and anything in the stack
		if len(stack) > 0 && last < len(stack)-1 {
			topSmall = stack[last+1]
			stack = stack[:last+1]
		}

		// add the current number to the stack after the popping
		stack = append(stack, i)
	}

	return false
}
