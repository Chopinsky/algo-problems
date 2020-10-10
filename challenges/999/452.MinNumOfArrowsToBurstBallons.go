package challenges

import "sort"

func findMinArrowShots(points [][]int) int {
	size := len(points)
	if size <= 1 {
		return size
	}

	sort.Slice(points, func(i, j int) bool {
		if points[i][0] == points[j][0] {
			return points[i][1] < points[j][1]
		}

		return points[i][0] < points[j][0]
	})

	// fmt.Println(points)

	dp := make([][]int, 0, size)
	dp = append(dp, points[0])
	idx := 0

	for i := 1; i < size; i++ {
		if points[i][0] <= dp[idx][1] {
			dp[idx][0] = points[i][0]

			if points[i][1] < dp[idx][1] {
				dp[idx][1] = points[i][1]
			}

			continue
		}

		dp = append(dp, points[i])
		idx++
	}

	// fmt.Println(dp)

	return len(dp)
}
