package challenges

import (
	"fmt"
	"sort"
)

func eraseOverlapIntervals(intervals [][]int) int {
	if intervals == nil || len(intervals) <= 1 {
		return 0
	}

	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})

	end := -1 * 1 << 31
	count := 0

	for _, v := range intervals {
		if end <= v[0] {
			end = v[1]
		} else {
			count++
		}
	}

	return count
}

func eraseOverlapIntervals1(intervals [][]int) int {
	if intervals == nil || len(intervals) <= 1 {
		return 0
	}

	size := len(intervals)
	dp := make([][]int, size)

	for i := range dp {
		dp[i] = make([]int, 2)
	}

	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][1] == intervals[j][1] {
			return intervals[i][0] < intervals[j][0]
		}

		return intervals[i][1] < intervals[j][1]
	})

	dp[0][1] = 1

	for i := 1; i < size; i++ {
		// if remove self, plus 1
		dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1

		last := find(intervals, i)
		if last < 0 {
			// needs to remove all points from the start to `i-1`
			dp[i][0] = i
		} else {
			// min remove from position `last`, plust the arrays between `last` and `i`
			dp[i][0] = min(dp[last][0], dp[last][1]) + (i - 1 - last)
		}
	}

	fmt.Println(intervals)
	fmt.Println(dp)

	return min(dp[size-1][0], dp[size-1][1])
}

func find(arr [][]int, idx int) int {
	start := arr[idx][0]
	if arr[0][1] > start {
		return -1
	}

	l, r := 0, idx
	for l < r {
		m := (l + r) / 2
		if arr[m][1] <= start {
			l = m
			break
		}

		if arr[m][1] < start {
			l = m + 1
		} else {
			r = m - 1
		}
	}

	for {
		if l < idx-1 && arr[l+1][1] <= start {
			l++
			continue
		}

		break
	}

	for {
		if l > 0 && arr[l][1] > start {
			l--
			continue
		}

		break
	}

	return l
}

func min(a, b int) int {
	if a <= b {
		return a
	}

	return b
}
