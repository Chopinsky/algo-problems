package challenges

/**
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
*/

func canPlaceFlowers(flowerbed []int, n int) bool {
	if n <= 0 {
		return true
	}

	size := len(flowerbed)
	if size == 1 {
		return flowerbed[0] == 0 && n <= 1
	}

	var running, total int

	for i, val := range flowerbed {
		if val == 0 {
			running++

			if i == 0 || i == size-1 {
				running++
			}

			// early exit
			if running > 2 && total+(running-1)/2 >= n {
				return true
			}

			continue
		}

		if running > 2 {
			total += (running - 1) / 2
		}

		// early exit
		if total >= n {
			return true
		}

		running = 0
	}

	if running > 2 {
		total += (running - 1) / 2
	}

	return total >= n
}
