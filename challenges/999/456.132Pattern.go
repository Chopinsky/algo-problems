package challenges

func find132pattern(nums []int) bool {
	if nums == nil || len(nums) < 3 {
		return false
	}

	// stack is the mono-decreasing stack, which stores larger
	// numbers to the right of the current cursor
	stack := make([]int, 0, len(nums))
	// this will be the index for the number of index j
	topSmall := -1

	for i := len(nums) - 1; i >= 0; i-- {
		n := nums[i]

		// if there's ever a number popped out, meaning we have the
		// "32" pattern somewhere already, check the "13" part and we're
		// done
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

		if len(stack) > 0 && last < len(stack)-1 {
			topSmall = stack[last+1]
			stack = stack[:last+1]
		}

		stack = append(stack, i)
	}

	return false
}
