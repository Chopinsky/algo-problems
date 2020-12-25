package challenges

func findDiagonalOrder(matrix [][]int) []int {
	if matrix == nil || len(matrix) == 0 || len(matrix[0]) == 0 {
		return nil
	}

	h, w := len(matrix), len(matrix[0])
	ans := make([]int, 0, h*w)

	sum := 0
	dir := -1
	var j, i0, i1 int

	for sum < h+w-1 {
		if dir < 0 {
			if sum <= h-1 {
				i0 = sum
			} else {
				i0 = h - 1
			}

			i1 = -1
		} else {
			if sum <= w-1 {
				i0 = 0
			} else {
				i0 = sum - w + 1
			}

			i1 = h
		}

		// fmt.Println("diagnal:", sum, i0, i1)

		for i := i0; i != i1; i += dir {
			j = sum - i

			// fmt.Println(i, j)

			if j < 0 || j >= w {
				break
			}

			ans = append(ans, matrix[i][j])
		}

		dir *= -1
		sum++
	}

	return ans
}
