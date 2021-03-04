package challenges

import "fmt"

func searchMatrix2(matrix [][]int, target int) bool {
	if matrix == nil || len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}

	h, w := len(matrix), len(matrix[0])

	if target < matrix[0][0] || target > matrix[h-1][w-1] {
		return false
	}

	if target <= matrix[0][w-1] {
		return searchRow(matrix[0], target, w)
	}

	if target >= matrix[h-1][0] {
		return searchRow(matrix[h-1], target, w)
	}

	l, r := 0, h
	for l < r {
		m := (l + r) / 2

		if target < matrix[m][0] {
			r = m - 1
		} else if target > matrix[m][w-1] {
			l = m + 1
		} else {
			return searchRow(matrix[m], target, w)
		}
	}

	if l >= 0 && l < h {
		return searchRow(matrix[l], target, w)
	}

	fmt.Println("not found:", l)

	return false
}

func searchRow(row []int, val, size int) bool {
	l, r := 0, size
	for l < r {
		m := (l + r) / 2

		if row[m] == val {
			return true
		}

		if row[m] < val {
			l = m + 1
		} else if row[m] > val {
			r = m - 1
		}
	}

	if l < size && l >= 0 && row[l] == val {
		return true
	}

	fmt.Println("not found row:", l, row)

	return false
}
