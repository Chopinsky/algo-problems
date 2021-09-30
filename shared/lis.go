package shared

import "sort"

// FindLIS ...
func FindLIS(nums []int) []int {
	lis := make([]int, len(nums))
	icNums := make([]int, 0, len(nums))

	for i, n := range nums {
		// find the position to replace
		pos := sort.SearchInts(icNums, n)

		// the length (including self) of the increasing sequence
		lis[i] = pos + 1

		if pos == len(icNums) {
			// if insert to the last, append
			icNums = append(icNums, n)
		} else {
			// otherwise, replace the number
			icNums[pos] = n
		}
	}

	// fmt.Println(lis)

	return lis
}

// FindLIS1 ...
func FindLIS1(src []int) (int, []int) {
	ans := make([]int, len(src))
	for i := range ans {
		ans[i] = 1
	}

	m := 1
	for i := 1; i < len(src); i++ {
		for j := 0; j < i; j++ {
			if src[i] > src[j] {
				ans[i] = max(ans[i], ans[j]+1)
			}

			if ans[i] > m {
				m = ans[i]
			}
		}
	}

	return m, ans
}

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
