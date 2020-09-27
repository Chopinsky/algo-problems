package challenges

var dirs = []int{-1, 0, 1, 0, -1}

func containsCycle(grid [][]byte) bool {
	// use stack and depth
	h, w := len(grid), len(grid[0])
	if h*w < 4 {
		return false
	}

	visited := make([][]bool, h)
	depth := make([][]int, h)

	for i := range visited {
		visited[i] = make([]bool, w)
		depth[i] = make([]int, w)
	}

	stack := [][]int{}
	found := false

	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if visited[i][j] {
				continue
			}

			found, stack = walk(grid, stack, depth, visited, i, j, h, w)

			if found {
				return true
			}

			depth[i][j] = 0
		}
	}

	return false
}

func walk(grid [][]byte, stack, depth [][]int, visited [][]bool, i, j, h, w int) (bool, [][]int) {
	depth[i][j] = 1
	visited[i][j] = true
	stack = append(stack, []int{i, j, 0, 1})
	target := grid[i][j]

	// fmt.Println("====> ", string(target), i, j)

	for len(stack) > 0 {
		curr := stack[len(stack)-1]
		x, y, dir, d := curr[0], curr[1], curr[2], curr[3]
		done := true

		visited[x][y] = true
		depth[x][y] = d

		// fmt.Println("at node:", x, y, dir, d)

		for k := dir; k < 4; k++ {
			x0, y0 := x+dirs[k], y+dirs[k+1]

			// out of the grid
			if x0 < 0 || y0 < 0 || x0 >= h || y0 >= w || grid[x0][y0] != target {
				continue
			}

			// we loop back onto a visited node
			if visited[x0][y0] {
				// if the node is in the path and has been visited, found and done
				if depth[x0][y0] != 0 && d-depth[x0][y0] >= 3 {

					// fmt.Println(x0, y0)
					// fmt.Println(visited)
					// fmt.Println(depth)

					return true, nil
				}

				// not the desired node or visited, continue
				continue
			}

			//todo: push this node to the stack, and continue
			stack = append(stack, []int{x0, y0, 0, d + 1})
			done = false
			curr[2] = k + 1

			break
		}

		// pop, and reset the depth if all other nodes from this node have been visited
		if done {
			depth[x][y] = 0
			stack = stack[:len(stack)-1]
		}
	}

	return false, stack
}
