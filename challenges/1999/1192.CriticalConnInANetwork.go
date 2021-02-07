package challenges

import "fmt"

func criticalConnections(n int, connections [][]int) [][]int {
	graph := make([][]int, n)

	for _, k := range connections {
		graph[k[0]] = append(graph[k[0]], k[1])
		graph[k[1]] = append(graph[k[1]], k[0])
	}

	level := make([]int, n)
	root := make([]int, n)

	var ans [][]int
	ans, _ = dfsCCN(0, -1, 1, graph, [][]int{}, level, root)

	return ans
}

func dfsCCN(u, parent, l int, graph, ans [][]int, level, root []int) ([][]int, int) {
	level[u] = l
	root[u] = l
	l++

	for _, v := range graph[u] {
		// don't revisit the parent again which will cause the circlular
		// calls
		if parent == v {
			continue
		}

		// the starting id == 1, so if level[v] == 0, meaning the node has
		// not been visited before; now build the network from v.
		if level[v] == 0 {
			ans, l = dfsCCN(v, u, l, graph, ans, level, root)

			// if the subtree of v can't get around to u in an alt route,
			// meaning the [u, v] edge is the critical path
			if level[u] < root[v] {
				ans = append(ans, []int{u, v})
			}

			// update the root level to the lowest level available in this
			// network
			root[u] = min(root[u], root[v])
		} else {
			// if the node v have already been visited, update with the
			// smallest root level, and effectively adding the node u
			// to the network
			root[u] = min(root[u], level[v])
		}
	}

	return ans, l
}

func criticalConnections1(n int, conn [][]int) [][]int {
	edges := make(map[int][]int)

	for _, e := range conn {
		edges[e[0]] = append(edges[e[0]], e[1])
		edges[e[1]] = append(edges[e[1]], e[0])
	}

	fmt.Println(edges)

	ans := [][]int{}
	visited := make([]bool, n)
	lvl := make([]int, n)
	root := make([]int, n)
	parent := make([]int, n)

	for i := range parent {
		parent[i] = -1
	}

	currLvl := 0
	for i := 0; i < n; i++ {
		if visited[i] {
			continue
		}

		ans, currLvl = build(i, currLvl, edges, parent, lvl, root, visited, ans)
	}

	// fmt.Println(parent, visited)

	return ans
}

func build(u, curr int, edges map[int][]int, parent, lvl, root []int, visited []bool, c [][]int) ([][]int, int) {
	visited[u] = true

	lvl[u] = curr
	root[u] = curr

	curr++

	if adj, ok := edges[u]; ok && len(adj) > 0 {
		for _, v := range adj {
			if !visited[v] {
				parent[v] = u
				c, curr = build(v, curr, edges, parent, lvl, root, visited, c)

				root[u] = min(root[u], root[v])

				if root[v] > lvl[u] {
					c = append(c, []int{u, v})
				}
			} else if v != parent[u] {
				// build the bridge, and connect the roots
				root[u] = min(root[u], lvl[v])
			}
		}
	}

	return c, curr
}
