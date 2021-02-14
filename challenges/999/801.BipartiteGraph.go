package challenges

func isBipartite(graph [][]int) bool {
	set := make([]int, len(graph))

	for i := range graph {
		if set[i] > 0 {
			continue
		}

		canPaint := paint(graph, set, i)
		if !canPaint {
			return false
		}
	}

	return true
}

func paint(graph [][]int, set []int, root int) bool {
	v := make([]int, 0, len(graph))
	v = append(v, root)

	next := make([]int, 0, len(graph))
	nextVal := 1

	for len(v) > 0 {
		for _, i := range v {
			if set[i] == 0 {
				set[i] = nextVal
				next = append(next, graph[i]...)
				continue
			}

			if set[i] != nextVal {
				return false
			}
		}

		v, next = next, v
		next = next[:0]
		nextVal *= -1
	}

	return true
}
