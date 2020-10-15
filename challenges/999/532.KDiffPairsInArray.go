package challenges

func findPairs(nums []int, k int) int {
	m := make(map[int]int)
	for _, val := range nums {
		m[val]++
	}

	ans := 0

	if k == 0 {
		for _, v := range m {
			if v > 1 {
				ans++
			}
		}

		return ans
	}

	for n := range m {
		if _, ok := m[n+k]; ok {
			ans++
		}
	}

	return ans
}
