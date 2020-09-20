package challenges

/**
Problem: Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Example 1:

Input: [2,2,3,2]
Output: 3

Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

Solution: For every number, the bit 1 will appear 3x times at positions from numbers that do appear 3 times in the array; for the single number, the bit 1 will appear 3x + 1 times. We will single out such bits and regenerate the number from theme.
*/
func singleNumber(nums []int) int {
	result := 0
	bit := 1
	sum := 0

	for i := 0; i < 64; i++ {
		sum = 0

		for _, num := range nums {
			if (num & bit) != 0 {
				sum++
			}
		}

		if sum%3 == 1 {
			result |= bit
		}

		bit = bit << 1
	}

	return result
}

/**
This is the abstract version from the same solution as above
*/
func singleNumber2(nums []int) int {
	once := 0
	twice := 0

	for _, num := range nums {
		once = ^twice & (once ^ num)
		twice = ^once & (twice ^ num)
	}

	return once
}
