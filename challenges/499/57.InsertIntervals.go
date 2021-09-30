package challenges

func insert(intervals [][]int, newInterval []int) [][]int {
	if intervals == nil || len(intervals) == 0 {
		return [][]int{newInterval}
	}

	if newInterval == nil || len(newInterval) == 0 {
		return intervals
	}

	size := len(intervals)
	s, e := newInterval[0], newInterval[1]

	// merge with the head
	if s <= intervals[0][1] {
		if e < intervals[0][0] {
			ans := make([][]int, size+1)
			ans[0] = newInterval
			copy(ans[1:], intervals)

			return ans
		}

		if s < intervals[0][0] {
			intervals[0][0] = s
		}

		if e > intervals[0][1] {
			intervals[0][1] = e
			return merge(intervals, 0, size)
		}

		return intervals
	}

	// merge with the tail
	if s >= intervals[size-1][0] {
		if s > intervals[size-1][1] {
			intervals = append(intervals, newInterval)
			return intervals
		}

		if e > intervals[size-1][1] {
			intervals[size-1][1] = e
		}

		return intervals
	}

	l, r := 1, size

	for l < r {
		m := (l + r) / 2
		// fmt.Println(l, m, r)

		if s > intervals[m][0] {
			l = m + 1
		}

		if s <= intervals[m][0] {
			r = m - 1
		}
	}

	if s > intervals[l][0] {
		l++
	}

	// fmt.Println(l, s, e)

	if s <= intervals[l-1][1] {
		if e > intervals[l-1][1] {
			intervals[l-1][1] = e
			return merge(intervals, l-1, size)
		}

		return intervals
	}

	if e >= intervals[l][0] {
		if s < intervals[l][0] {
			intervals[l][0] = s
		}

		if e > intervals[l][1] {
			intervals[l][1] = e
			return merge(intervals, l, size)
		}

		return intervals
	}

	ans := make([][]int, size+1)

	copy(ans, intervals[:l])
	ans[l] = newInterval
	copy(ans[l+1:], intervals[l:])

	return ans
}

func merge(it [][]int, l, size int) [][]int {
	r := l + 1

	for r < size {
		if it[r][0] > it[l][1] {
			break
		}

		if it[r][1] > it[l][1] {
			it[l][1] = it[r][1]
		}

		r++
	}

	if r > l+1 {
		diff := r - l - 1
		copy(it[l+1:], it[r:])
		it = it[:(size - diff)]
	}

	return it
}
