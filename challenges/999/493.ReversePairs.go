package challenges

/**
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2

Example2:

Input: [2,4,3,5,1]
Output: 3
*/

func reversePairs(nums []int) int {
	c := mergeCountRP(nums, 0, len(nums)-1)
	// fmt.Println(nums)
	return c
}

func mergeCountRP(nums []int, l, r int) int {
	if l >= r {
		return 0
	}

	mid := (l + r) / 2
	count := mergeCountRP(nums, l, mid) + mergeCountRP(nums, mid+1, r)

	j := mid + 1
	for i := l; i <= mid; i++ {
		for j <= r && int64(nums[i]) > int64(nums[j])*2 {
			j++
		}

		count += j - (mid + 1)
	}

	mergeRP(nums, l, mid, r)

	return count
}

func mergeRP(nums []int, l, m, r int) {
	la, ra := make([]int, m-l+1), make([]int, r-m)
	copy(la, nums[l:m+1])
	copy(ra, nums[m+1:r+1])

	// fmt.Println(la, ra)

	var il, ir int

	for i := l; i <= r; i++ {
		if ir >= len(ra) || (il < len(la) && la[il] <= ra[ir]) {
			nums[i] = la[il]
			il++
		} else {
			nums[i] = ra[ir]
			ir++
		}
	}
}
