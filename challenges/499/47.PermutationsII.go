package challenges

import "fmt"

func permuteUnique(nums []int) [][]int {
	if len(nums) == 1 {
		return [][]int{nums}
	}

	counts := make(map[int]int)
	for _, n := range nums {
		counts[n]++
	}

	// return permute1(nums, make([][]int, 0, 256), make(map[string]bool), 0, len(nums))
	return permute(make([]int, 0, len(nums)), make([][]int, 0, 256), counts, len(nums))
}

func permute(row []int, ans [][]int, counts map[int]int, size int) [][]int {
	if len(row) == size {
		next := make([]int, size)
		copy(next, row)

		ans = append(ans, next)
		return ans
	}

	for n, c := range counts {
		if c == 0 {
			continue
		}

		row = append(row, n)
		counts[n]--

		ans = permute(row, ans, counts, size)

		row = row[:len(row)-1]
		counts[n]++
	}

	return ans
}

func permute1(nums []int, ans [][]int, cache map[string]bool, i, size int) [][]int {
	if i >= size {
		key := fmt.Sprint(nums)
		if !cache[key] {
			cache[key] = true
			ans = append(ans, nums)
		}

		return ans
	}

	ans = permute1(nums, ans, cache, i+1, size)

	for j := i + 1; j < size; j++ {
		if nums[i] == nums[j] {
			continue
		}

		next := make([]int, size)
		copy(next, nums)

		next[i], next[j] = next[j], next[i]
		ans = permute1(next, ans, cache, i+1, size)
	}

	return ans
}
