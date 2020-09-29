package challenges

func findMaximumXOR(nums []int) int {
	ans := 0
	tgt := 0
	mask := 0

	for i := 31; i >= 0; i-- {
		// use mask to extract top digits of the number
		mask |= (1 << i)

		// the target is the next largest possible value
		tgt = ans | (1 << i)

		// create the store on the numbers through the mask
		dp := make(map[int]bool)

		// go through the numbers list, and check
		for _, val := range nums {
			// if we already have a number, whose top digits ^ this number's top
			// digits will yield the target answer, we found the match, update
			// states and continue to the next digit
			if dp[(val&mask)^tgt] {
				ans = tgt
				break
			} else {
				// we haven't found the match, store the top digitis as available
				dp[(val & mask)] = true
			}
		}
	}

	return ans
}

func findMaximumXOR1(nums []int) int {
	best := 0
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			val := nums[i] ^ nums[j]
			if val > best {
				best = val
			}
		}
	}

	return best
}
