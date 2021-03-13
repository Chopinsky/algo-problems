package challenges

/**
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Constraints:

0 <= n, m <= 200
1 <= n + m <= 200
nums1.length == m + n
nums2.length == n
-109 <= nums1[i], nums2[i] <= 109
*/

func mergeSorted(nums1 []int, m int, nums2 []int, n int) {
	if n == 0 {
		return
	}

	stack := make([]int, 0, m)
	var j int

	for i := range nums1 {
		// fmt.Println(i, j, stack, nums1)

		if j >= n {
			if i < m {
				stack = append(stack, nums1[i])
			}

			nums1[i] = stack[0]
			stack = stack[1:]
			continue
		}

		if len(stack) == 0 {
			// fmt.Println("stack 0:", i, m, stack)

			if i >= m {
				nums1[i] = nums2[j]
				j++
				continue
			}

			if nums1[i] <= nums2[j] {
				continue
			}

			stack = append(stack, nums1[i])
			nums1[i] = nums2[j]
			j++

			continue
		}

		if i < m {
			stack = append(stack, nums1[i])
		}

		if j >= n || stack[0] <= nums2[j] {
			nums1[i] = stack[0]
			stack = stack[1:]
			continue
		}

		nums1[i] = nums2[j]
		j++
	}

	// fmt.Println(stack, j)
}
