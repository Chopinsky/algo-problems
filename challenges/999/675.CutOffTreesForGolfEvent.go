package challenges

import (
	"fmt"
	"sort"
)

var dirs = []int{-1, 0, 1, 0, -1}

func cutOffTree(forest [][]int) int {
	if forest[0][0] == 0 {
		return -1
	}

	h, w := len(forest), len(forest[0])
	dots := make([][]int, 0, h*w)

	for i := range forest {
		for j := range forest[i] {
			if forest[i][j] == 0 {
				continue
			}

			k := toKey(i, j, w)
			dots = append(dots, []int{forest[i][j], k})
		}
	}

	sort.Slice(dots, func(i, j int) bool {
		return dots[i][0] < dots[j][0]
	})

	fmt.Println(dots)

	if len(dots) == 1 {
		return 0
	}

	dist := make([][]int, h*w)
	for i := range dist {
		dist[i] = make([]int, h*w)
	}

	steps := walkDist(0, dots[0][1], h, w, forest, dist)
	if steps < 0 {
		return -1
	}

	fmt.Println(dots[0][1], steps)

	for i := 1; i < len(dots); i++ {
		next := walkDist(dots[i-1][1], dots[i][1], h, w, forest, dist)

		fmt.Println(dots[i-1][1], "->", dots[i][1], next)

		if next == -1 {
			return -1
		}

		steps += next
	}

	// fmt.Println(dist)

	return steps
}

func walkDist(from, to, h, w int, f, dist [][]int) int {
	if from == to {
		return 0
	}

	if dist[from][to] > 0 {
		return dist[from][to]
	}

	ans := 0
	steps := 1

	stack := []int{}
	visited := map[int]bool{
		from: true,
	}

	var x, y, x0, y0, k int
	x, y = fromKey(from, w)

	for i := 0; i < 4; i++ {
		x0, y0 = x+dirs[i], y+dirs[i+1]
		if x0 < 0 || x0 >= h || y0 < 0 || y0 >= w || f[x0][y0] == 0 {
			continue
		}

		k = toKey(x0, y0, w)
		if k == to {
			dist[from][to] = 1
			return 1
		}

		visited[k] = true

		if dist[k][to] > 0 && (ans == 0 || dist[k][to]+steps < ans) {
			ans = dist[k][to] + steps
		} else {
			stack = append(stack, k)
		}
	}

	for len(stack) > 0 {
		next := make([]int, 0, len(stack))
		done := false
		steps++

		for _, v := range stack {
			x, y = fromKey(v, w)

			for i := 0; i < 4; i++ {
				x0, y0 = x+dirs[i], y+dirs[i+1]
				if x0 < 0 || x0 >= h || y0 < 0 || y0 >= w || f[x0][y0] == 0 {
					continue
				}

				k = toKey(x0, y0, w)
				if k == from || visited[k] {
					continue
				}

				if k == to {
					done = true
					if ans == 0 || ans > steps {
						ans = steps
					}

					break
				}

				visited[k] = true

				if dist[k][to] > 0 && (ans == 0 || dist[k][to]+steps < ans) {
					ans = dist[k][to] + steps
				} else {
					next = append(next, k)
				}
			}

			if done {
				break
			}
		}

		if done {
			break
		}

		// fmt.Println(next)

		stack = next
	}

	if ans == 0 {
		ans = -1
	}

	dist[from][to] = ans

	return ans
}
