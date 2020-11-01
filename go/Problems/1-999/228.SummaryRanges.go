package challenges

func summaryRanges(nums []int) []string {
	if nums == nil || len(nums) == 0 {
		return nil
	}

	l, r := 0, 0
	ans := make([]string, 0, len(nums))

	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1]+1 {
			r++
			continue
		}

		if l == r {
			ans = append(ans, fmt.Sprintf("%d", nums[l]))
		} else {
			ans = append(ans, fmt.Sprintf("%d->%d", nums[l], nums[r]))
		}

		l = i
		r = i
	}

	if l == r {
		ans = append(ans, fmt.Sprintf("%d", nums[l]))
	} else {
		ans = append(ans, fmt.Sprintf("%d->%d", nums[l], nums[r]))
	}

	return ans
}
