package challenges

import "sort"

/**
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
*/

func diagonalSort(mat [][]int) [][]int {
	h, w := len(mat), len(mat[0])
	if h == 1 || w == 1 {
		return mat
	}

	stack := make([]int, 0, max(h, w))

	for i := h - 2; i > 1-w; i-- {
		if i >= 0 {
			for j := i; j < h && j-i < w; j++ {
				stack = append(stack, mat[j][j-i])
			}

			sort.Ints(stack)

			for j, idx := i, 0; j < h && j-i < w; j++ {
				mat[j][j-i] = stack[idx]
				idx++
			}
		} else {
			for j := -i; j < w && j+i < h; j++ {
				// fmt.Println(j, j+i)
				stack = append(stack, mat[j+i][j])
			}

			sort.Ints(stack)

			for j, idx := -i, 0; j < w && j+i < h; j++ {
				mat[j+i][j] = stack[idx]
				idx++
			}
		}

		stack = stack[:0]
	}

	return mat
}
