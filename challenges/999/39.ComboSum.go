package challenges

import "sort"

func combinationSum(candidates []int, target int) [][]int {
	sort.Ints(candidates)

	ans := make([][]int, 0, len(candidates))
	for i, val := range candidates {
		if val == target {
			ans = append(ans, []int{val})
			break
		}

		if val > target {
			break
		}

		sum := val
		arr := make([]int, 0, target/val+1)
		arr = append(arr, val)

		for sum < target {
			res := calc(sum, i+1, target, candidates, arr)

			if res != nil && len(res) > 0 {
				ans = append(ans, res...)
			}

			sum += val
			arr = append(arr, val)
		}

		if sum == target {
			ans = append(ans, arr)
		}
	}

	return ans
}

func calc(sum, i, target int, nums, curr []int) [][]int {
	if i >= len(nums) {
		return nil
	}

	ans := make([][]int, 0, len(curr))
	arr := make([]int, len(curr))
	copy(arr, curr)

	for sum < target {
		res := calc(sum, i+1, target, nums, arr)
		if res != nil && len(res) > 0 {
			ans = append(ans, res...)
		}

		sum += nums[i]
		arr = append(arr, nums[i])
	}

	if sum == target {
		ans = append(ans, arr)
	}

	return ans
}
