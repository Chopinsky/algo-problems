package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// RMNEKGCProblems ...
type RMNEKGCProblems struct {
	set []*RMNEKGC
}

// Solve ...
func (p *RMNEKGCProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm finished in:", time.Since(start))
}

// RMNEKGC ...
type RMNEKGC struct {
	data   [][]int
	n      int
	output int
}

// CreateRMNEKGC ...
func CreateRMNEKGC() s.Problem {
	set := make([]*RMNEKGC, 0, 4)

	set = append(set, &RMNEKGC{
		data: [][]int{
			{3, 1, 2},
			{3, 2, 3},
			{1, 1, 3},
			{1, 2, 4},
			{1, 1, 2},
			{2, 3, 4},
		},
		n:      4,
		output: 2,
	})

	set = append(set, &RMNEKGC{
		data: [][]int{
			{3, 1, 2},
			{3, 2, 3},
			{1, 1, 4},
			{2, 1, 4},
		},
		n:      4,
		output: 0,
	})

	set = append(set, &RMNEKGC{
		data: [][]int{
			{3, 2, 3},
			{1, 1, 2},
			{2, 3, 4},
		},
		n:      4,
		output: -1,
	})

	return &RMNEKGCProblems{set}
}

func (p *RMNEKGC) solve() int {
	n, g := p.n, p.data

	a := make([][]int, 0, len(p.data))
	b := make([][]int, 0, len(p.data))

	sort.Slice(g, func(i, j int) bool {
		if g[i][0] == g[j][0] {
			if g[i][1] == g[j][1] {
				return g[i][2] < g[j][2]
			}

			return g[i][1] < g[j][1]
		}

		return g[i][0] > g[j][0]
	})

	// fmt.Println(g)

	e := make([][]int, n+1)

	for i := range e {
		e[i] = make([]int, n+1)
	}

	count := 0

	for i := range g {
		u, v := g[i][1], g[i][2]

		if u > v {
			g[i][1] = v
			g[i][2] = u
			u, v = v, u
		}

		if g[i][0] == 1 {
			if e[u][v] >= 0 {
				a = append(a, g[i])
			} else {
				count++
			}
		} else if g[i][0] == 2 {
			if e[u][v] >= 0 {
				b = append(b, g[i])
			} else {
				count++
			}
		} else {
			a = append(a, g[i])
			b = append(b, g[i])

			e[u][v] = -1
		}
	}

	ea := findExtraEdges(a, n)
	if ea == nil {
		return -1
	}

	eb := findExtraEdges(b, n)
	if eb == nil {
		return -1
	}

	if len(ea) == 0 && len(eb) == 0 {
		return count
	}

	shared := make(map[int]bool)
	for _, edge := range ea {
		// the edge can definitely be removed
		if edge[0] != 3 {
			count++
			continue
		}

		//todo: check if both share the same edge
		u, v := edge[1], edge[2]
		shared[u*n+v] = true
	}

	for _, edge := range eb {
		if edge[0] != 3 {
			count++
			continue
		}

		u, v := edge[1], edge[2]
		if shared[u*n+v] {
			count++
		}
	}

	if s.DebugMode() {
		fmt.Println("extras from a:", a, ea)
		fmt.Println("extras from b:", b, eb)
	}

	return count
}

func findExtraEdges(edges [][]int, n int) [][]int {
	ans := make([][]int, 0, len(edges))
	root := make([]int, n+1)

	for i := range root {
		root[i] = i
	}

	for _, e := range edges {
		ru, rv := findRoot(root, e[1]), findRoot(root, e[2])

		if ru != rv {
			if ru < rv {
				root[rv] = ru
			} else {
				root[rv] = ru
			}

			continue
		}

		ans = append(ans, e)
	}

	baseRoot := findRoot(root, 1)

	for i := 2; i <= n; i++ {
		if findRoot(root, i) != baseRoot {
			return nil
		}
	}

	return ans
}

func union(a []int, i, j int) {
	ri, rj := findRoot(a, i), findRoot(a, j)

	if ri < rj {
		a[rj] = ri
	} else {
		a[ri] = rj
	}
}

func findRoot(a []int, i int) int {
	for a[i] != i {
		i = a[i]
	}

	return i
}
