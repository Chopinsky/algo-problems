package challenges

/**
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
*/

func numIslands(grid [][]byte) int {
	h, w := len(grid), len(grid[0])

	visited := make([][]bool, h)
	for i := range visited {
		visited[i] = make([]bool, w)
	}

	count := 0
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if visited[i][j] {
				continue
			}

			if grid[i][j] == '1' {
				markIslands(grid, visited, i, j, h, w)
				count++
			}
		}
	}

	return count
}

func markIslands(grid [][]byte, visited [][]bool, i, j, h, w int) {
	points := make([]int, 0, h*w)
	points = append(points, toKey(i, j, w))
	dirs := []int{-1, 0, 1, 0, -1}

	var key int

	for len(points) > 0 {
		key, points = points[0], points[1:]
		x, y := fromKey(key, w)

		for i := 0; i < 4; i++ {
			x0, y0 := x+dirs[i], y+dirs[i+1]

			if x0 < 0 || x0 >= h || y0 < 0 || y0 >= w || grid[x0][y0] == '0' {
				continue
			}

			if visited[x0][y0] {
				continue
			}

			visited[x0][y0] = true
			points = append(points, toKey(x0, y0, w))
		}
	}
}

func toKey(i, j, w int) int {
	return i*w + j
}

func fromKey(k, w int) (int, int) {
	return k / w, k % w
}
