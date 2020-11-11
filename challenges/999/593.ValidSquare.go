package challenges

import "sort"

func validSquare(p1 []int, p2 []int, p3 []int, p4 []int) bool {
	points := [][]int{p1, p2, p3, p4}

	sort.Slice(points, func(i, j int) bool {
		if points[i][1] == points[j][1] {
			return points[i][0] < points[j][0]
		}

		return points[i][1] < points[j][1]
	})

	// fmt.Println(points)

	if points[0][1] == points[1][1] {
		if points[0][0] == points[1][0] || points[2][1] != points[3][1] || points[0][0] != points[2][0] || points[1][0] != points[3][0] || absDiff(points[0][0], points[1][0]) != absDiff(points[0][1], points[2][1]) {
			return false
		}

		return true
	}

	if points[1][1] == points[2][1] {
		if points[0][0] != points[3][0] || absDiff(points[0][1], points[3][1]) != absDiff(points[1][0], points[2][0]) {
			return false
		}

		if points[1][0]+points[2][0] != points[0][0]+points[3][0] || points[0][1]+points[3][1] != points[1][1]+points[2][1] {
			return false
		}

		return true
	}

	if points[1][0] > points[2][0] {
		if points[3][1]-points[0][1] != points[1][0]-points[2][0] || points[3][0]-points[0][0] != points[2][1]-points[1][1] {
			return false
		}

		return true
	}

	// points[1][0] < points[2][0]
	if points[0][0]-points[3][0] != points[2][1]-points[1][1] || points[3][1]-points[0][1] != points[2][0]-points[1][0] {
		return false
	}

	return true
}

func absDiff(a, b int) int {
	if a >= b {
		return a - b
	}

	return b - a
}
