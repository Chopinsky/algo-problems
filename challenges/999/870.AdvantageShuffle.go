package challenges

import "sort"

func advantageCount(a []int, b []int) []int {
	l := len(a)

	bval := make([]int, l)
	ans := make([]int, l)
	sa, sb := make([]int, l), make([]int, l)

	for i := range a {
		bval[i] = -1
		sa[i] = i
		sb[i] = i
	}

	sort.Slice(sa, func(i, j int) bool { return a[sa[i]] < a[sa[j]] })
	sort.Slice(sb, func(i, j int) bool { return b[sb[i]] < b[sb[j]] })

	// fmt.Println(sa, sb)
	last := l - 1

	for _, i := range sa {
		va := a[i]

		pos := sort.Search(l, func(j int) bool {
			return b[sb[j]] >= va
		}) - 1

		// find the position that has not been taken
		for pos >= 0 && bval[pos] >= 0 {
			pos--
		}

		if pos < 0 {
			for last >= 0 && bval[last] >= 0 {
				last--
			}

			bval[last] = va
			last--
		} else {
			bval[pos] = va
		}
	}

	for i, p := range bval {
		ans[sb[i]] = p
	}

	return ans
}
