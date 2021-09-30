package challenges

/**
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:

Input: nums = [1]
Output: [1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
*/

import "sort"

func nextPermutation(nums []int) {
	size := len(nums)
	if size <= 1 {
		return
	}

	for i := size - 2; i >= 0; i-- {
		if nums[i] >= nums[i+1] {
			continue
		}

		// fmt.Println("counting:", i)

		if i == size-2 {
			nums[i], nums[i+1] = nums[i+1], nums[i]
		} else {
			j := i + 1

			for j <= size {
				if j == size || nums[j] <= nums[i] {
					nums[i], nums[j-1] = nums[j-1], nums[i]
					break
				}

				j++
			}

			sort.Ints(nums[i+1:])
		}

		return
	}

	sort.Ints(nums)
}
