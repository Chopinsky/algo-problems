package challenges

/**
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
*/

import "sort"

func searchMatrix(matrix [][]int, target int) bool {
	h, w := len(matrix), len(matrix[0])
	i, j := 0, w-1

	for i < h && j >= 0 {
		if matrix[i][j] == target {
			return true
		}

		if matrix[i][j] > target {
			j--
		} else {
			i++
		}
	}

	return false
}

func searchMatrix1(matrix [][]int, target int) bool {
	h, w := len(matrix), len(matrix[0])
	if target < matrix[0][0] || target > matrix[h-1][w-1] {
		return false
	}

	lastCol := make([]int, 0, h)
	for _, r := range matrix {
		lastCol = append(lastCol, r[w-1])
	}

	// fmt.Println(lastCol)

	i0 := sort.SearchInts(lastCol, target)
	if i0 >= h {
		return false
	}

	j0 := sort.SearchInts(matrix[h-1], target)
	if j0 >= w {
		return false
	}

	// fmt.Println(i0, j0)

	for i := i0; i < h; i++ {
		pos := sort.SearchInts(matrix[i][j0:], target)
		if j0+pos < w && matrix[i][j0+pos] == target {
			return true
		}
	}

	return false
}
