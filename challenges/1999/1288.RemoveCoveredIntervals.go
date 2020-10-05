package challenges

import "sort"

func removeCoveredIntervals(intervals [][]int) int {
	size := len(intervals)
	if size == 1 {
		return 0
	}

	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] > intervals[j][1]
		}

		return intervals[i][0] < intervals[j][0]
	})

	// return getCount(intervals)

	// number of intervals that will be covered
	count := 0

	// the right bound defines the furthest location where
	// a previous interval can cover
	rightBound := intervals[0][1]

	for i := 1; i < size; i++ {
		// covered, add it to the count
		if intervals[i][1] <= rightBound {
			count++
			continue
		}

		// not covered by any previous intervals, update the bounds
		rightBound = intervals[i][1]
	}

	return size - count
}

func getCount(intervals [][]int) int {
	count := 0

	for i := 0; i < len(intervals); i++ {
		covered := false

		for j := i - 1; j >= 0; j-- {
			if intervals[j][1] >= intervals[i][1] {
				covered = true
				break
			}
		}

		// fmt.Println(intervals[i], covered)

		if !covered {
			count++
		}
	}

	return count
}
