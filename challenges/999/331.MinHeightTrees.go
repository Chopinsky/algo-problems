package challenges

func findMinHeightTrees(n int, edges [][]int) []int {
	if n == 1 || len(edges) == 0 {
		return []int{0}
	}

	if n == 2 || len(edges) == 1 {
		return []int{edges[0][0], edges[0][1]}
	}

	ec := make([]int, n)
	v := make([]map[int]bool, n)
	stack := make([]int, 0, n)

	for _, e := range edges {
		ec[e[0]]++
		ec[e[1]]++

		if v[e[0]] == nil {
			v[e[0]] = make(map[int]bool)
		}

		if v[e[1]] == nil {
			v[e[1]] = make(map[int]bool)
		}

		v[e[0]][e[1]] = true
		v[e[1]][e[0]] = true
	}

	// fmt.Println(v)
	leaf := make(map[int]bool)

	for i, conn := range ec {
		if conn == 1 {
			stack = append(stack, i)
			leaf[i] = true
		}
	}

	for len(leaf) > 0 {
		next := make(map[int]bool)

		for l := range leaf {
			for nb := range v[l] {
				delete(v[nb], l)

				if len(v[nb]) == 1 {
					next[nb] = true
				}
			}

			v[l] = nil
		}

		if len(next) == 0 {
			break
		}

		leaf = next
	}

	// fmt.Println(leaf)

	ans := make([]int, 0, 2)
	for l := range leaf {
		ans = append(ans, l)
	}

	return ans
}
