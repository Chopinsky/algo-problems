package challenges

// var dirs = []int{-1, 0, 1, 0, -1}

func uniquePathsIII(grid [][]int) int {
	h, w := len(grid), len(grid[0])
	if h*w == 1 {
		return 0
	}

	if h*w == 2 {
		return 1
	}

	visited := make([][]bool, h)
	for i := range visited {
		visited[i] = make([]bool, w)
	}

	// stack := make([][]int, 0, 400)
	count := 0

	var sx, sy int
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if grid[i][j] == 1 {
				sx, sy = i, j
			}

			if grid[i][j] == 0 || grid[i][j] == 2 {
				count++
			}
		}
	}

	return walkPath(sx, sy, 0, count, 0, h, w, grid, visited)
}

func walkPath(x, y, currLvl, totalLvl, count, h, w int, grid [][]int, visited [][]bool) int {
	if x < 0 || y < 0 || x >= h || y >= w || visited[x][y] || grid[x][y] == -1 {
		return count
	}

	if grid[x][y] == 2 && currLvl == totalLvl {
		count++
		return count
	}

	visited[x][y] = true

	for i := 0; i < 4; i++ {
		count = walkPath(x+dirs[i], y+dirs[i+1], currLvl+1, totalLvl, count, h, w, grid, visited)
	}

	visited[x][y] = false

	return count
}
