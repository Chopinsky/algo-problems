package shared

import "fmt"

// StrEdits ...
func StrEdits(a, b []string) int {
	n, m := len(a), len(b)
	max := n + m

	v := make([]int, 2*max+1)
	v[max+1] = 0

	var x, y, idx int

	for i := 0; i <= max; i++ {
		for j := -i; j <= i; j += 2 {
			idx = j + max

			if j == -i || (j != i && v[idx-1] < v[idx+1]) {
				x = v[idx+1]
			} else {
				x = v[idx-1] + 1
			}

			y = x - j

			// fmt.Println(x, y, v)

			for x < n && y < m && a[x] == b[y] {
				x++
				y++
			}

			v[idx] = x

			if x >= n && y >= n {
				return i
			}
		}
	}

	return max
}

type state struct {
	x     int
	y     int
	count int
	moves []string
}

func (s state) key(pad int) int {
	return s.x*pad + s.y
}

// StrDiffs ...
func StrDiffs(a, b []string) []string {
	fmt.Println(a, b)

	n, m := len(a), len(b)
	max := n + m

	stack := make([]state, 0, max)
	stack = append(stack, state{
		x:     0,
		y:     0,
		count: 0,
		moves: []string{},
	})

	visited := make(map[int]bool, max)
	var curr, best state

	for len(stack) > 0 {
		curr, stack = stack[0], stack[1:]
		key := curr.key(max)

		if visited[key] {
			continue
		}

		visited[key] = true
		x, y, count := curr.x, curr.y, curr.count
		moves := curr.moves

		if x == n-1 && y == m-1 {
			if a[x] == b[y] {
				return moves
			}

			fmt.Println(x, y, moves, stack)

			curr.count += 2
			if best.count > 0 && curr.count >= best.count {
				continue
			}

			curr.moves = append(curr.moves, fmt.Sprint(x, ",", y, ",", 1))

			best = curr
		}

		for x < n && y < m && a[x] == b[y] {
			// fmt.Println(x, y, a[x], b[y])
			moves = append(moves, fmt.Sprint(x, ",", y, ",", 0))
			x++
			y++
		}

		if x+1 < n {
			m := append([]string(nil), moves...)

			stack = append(stack, state{
				x:     x + 1,
				y:     y,
				count: count + 1,
				moves: append(m, fmt.Sprint(x, ",", y, ",", -1)),
			})
		}

		if y+1 < m {
			stack = append(stack, state{
				x:     x,
				y:     y + 1,
				count: count + 1,
				moves: append(moves, fmt.Sprint(x, ",", y, ",", 1)),
			})
		}
	}

	return best.moves
}
