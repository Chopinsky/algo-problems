package challenges

func maxProduct(nums []int) int {
	size := len(nums)

	if size == 0 {
		return 0
	}

	if size == 1 {
		return nums[0]
	}

	s := 0
	for s < size && nums[s] == 0 {
		s++
	}

	if s == size {
		return 0
	}

	var best, prod int
	first := -1
	lastZ := s - 1

	if s == 0 || nums[s] >= 0 {
		best = nums[s]
	} else {
		best = 0
	}

	for i, val := range nums {
		if val == 0 {
			if best < 0 {
				best = 0
			}

			if prod != 0 && prod > best {
				best = prod
			}

			if prod < 0 && first >= 0 && first < i-1 {
				// pop
				for j := lastZ + 1; j <= first; j++ {
					prod /= nums[j]
				}

				if prod > best {
					best = prod
				}
			}

			prod = 0
			first = -1
			lastZ = i

			continue
		}

		if prod == 0 {
			prod = val
		} else {
			prod *= val
		}

		if prod > best {
			best = prod
		}

		if val < 0 && first < 0 {
			first = i
		}
	}

	if prod < 0 && first >= 0 && first < size-1 {
		// pop
		for j := lastZ + 1; j <= first; j++ {
			prod /= nums[j]
		}

		if prod > best {
			best = prod
		}
	}

	return best
}
