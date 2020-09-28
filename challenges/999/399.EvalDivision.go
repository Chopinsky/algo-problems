package challenges

import "fmt"

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	edges := make(map[string]map[string]float64)

	for i, e := range equations {
		if edges[e[0]] == nil {
			edges[e[0]] = make(map[string]float64)
		}

		if edges[e[1]] == nil {
			edges[e[1]] = make(map[string]float64)
		}

		edges[e[0]][e[1]] = values[i]
		edges[e[1]][e[0]] = 1.0 / values[i]
	}

	fmt.Println(edges)

	ans := make([]float64, len(queries))
	size := len(edges)

	var base float64
	var next string

	for i, q := range queries {
		if edges[q[0]] == nil || edges[q[1]] == nil {
			ans[i] = -1.0
			continue
		}

		if q[0] == q[1] {
			ans[i] = 1.0
			continue
		}

		visited := make(map[string]float64)
		stack := make([]string, 0, size)

		stack = append(stack, q[0])
		visited[q[0]] = 1.0
		done := false

		for !done && len(stack) > 0 {
			next, stack = stack[0], stack[1:]
			base = visited[next]

			// fmt.Println("details:", next, base, edges[next])

			for k, v := range edges[next] {
				if _, ok := visited[k]; ok {
					continue
				}

				// fmt.Println(next, k)

				if k == q[1] {
					ans[i] = base * v
					done = true

					edges[q[0]][q[1]] = ans[i]
					edges[q[1]][q[0]] = 1.0 / ans[i]

					break
				} else {
					stack = append(stack, k)
					visited[k] = base * v
				}
			}
		}

		if !done {
			ans[i] = -1.0
		}
	}

	return ans
}
