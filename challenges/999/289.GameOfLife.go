package challenges

func gameOfLife(board [][]int) {
	h, w := len(board), len(board[0])
	dirs := [][]int{
		{-1, -1}, {-1, 0}, {-1, 1},
		{0, -1}, {0, 1},
		{1, -1}, {1, 0}, {1, 1},
	}

	next := make([][]int, h)
	for i := range next {
		next[i] = make([]int, w)
	}

	for i := range board {
		for j := range board[i] {
			count := 0

			for _, d := range dirs {
				x, y := i+d[0], j+d[1]

				if x < 0 || x >= h || y < 0 || y >= w {
					continue
				}

				if board[x][y] == 1 {
					count++
				}
			}

			if board[i][j] == 0 && count == 3 {
				next[i][j] = 1
				continue
			}

			if board[i][j] == 1 && (count == 2 || count == 3) {
				next[i][j] = 1
				continue
			}
		}
	}

	for i := range next {
		for j, val := range next[i] {
			board[i][j] = val
		}
	}
}
