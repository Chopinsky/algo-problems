package challenges

/**
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]
*/

func generateMatrix(n int) [][]int {
	grid := make([][]int, n)
	for i := range grid {
		grid[i] = make([]int, n)
	}

	val := 1
	i0, i1 := 0, n-1
	j0, j1 := 0, n-1

	for i0 <= i1 {
		if i0 == i1 && j0 == j1 {
			grid[i0][i1] = val
			break
		}

		// top
		for j := j0; j < j1; j++ {
			grid[i0][j] = val
			val++
		}

		// right
		for i := i0; i < i1; i++ {
			grid[i][j1] = val
			val++
		}

		// bottom
		for j := j1; j > j0; j-- {
			grid[i1][j] = val
			val++
		}

		// left
		for i := i1; i > i0; i-- {
			grid[i][j0] = val
			val++
		}

		i0++
		i1--

		j0++
		j1--
	}

	return grid
}
