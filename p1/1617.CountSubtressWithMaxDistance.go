package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// CSWMDProblems ...
type CSWMDProblems struct {
	set []*CSWMD
}

// Solve ...
func (p *CSWMDProblems) Solve() {
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

// CSWMD ...
type CSWMD struct {
	data   [][]int
	n      int
	output []int
}

// CreateCSWMD ...
func CreateCSWMD() s.Problem {
	set := make([]*CSWMD, 0, 4)

	set = append(set, &CSWMD{
		data: [][]int{
			{1, 2}, {2, 3}, {2, 4},
		},
		n:      4,
		output: []int{3, 4, 0},
	})

	set = append(set, &CSWMD{
		data: [][]int{
			{1, 2},
		},
		n:      2,
		output: []int{1},
	})

	set = append(set, &CSWMD{
		data: [][]int{
			{1, 2}, {2, 3},
		},
		n:      3,
		output: []int{2, 1},
	})

	return &CSWMDProblems{set}
}

func (p *CSWMD) solve() []int {
	n, edges := p.n, p.data
	if n == 2 && len(edges) == 1 {
		return []int{1}
	}

	ans := make([]int, n-1)
	dist := make([][]int, n)
	e := make(map[int][]int)

	for i := range dist {
		dist[i] = make([]int, n)
	}

	for _, edge := range edges {
		a, b := edge[0]-1, edge[1]-1
		dist[a][b] = 1
		dist[b][a] = 1
		e[a] = append(e[a], b)
		e[b] = append(e[b], a)
	}

	subTrees := make([][]int, n)
	for i := 0; i < n; i++ {
		populateDistGrid(dist, e, i, n)

		for j := i + 1; j < n; j++ {
			d := dist[i][j]
			if d > 0 {
				subTrees[d-1] = append(subTrees[d-1], (1<<i + 1<<j))
			}
		}
	}

	// fmt.Println(subTrees)

	// d - max distance between cities
	for d := 1; d < n; d++ {
		trees := make(map[int]bool)
		st := subTrees[d-1]

		for _, t := range st {
			trees[t] = true
		}

		for idx := 0; idx < len(st); idx++ {
			// get the current tree to extend
			t := st[idx]

			// check every node if it can extend the underlying
			// subtree
			for j := 0; j < n; j++ {
				// node j is already in the subtree, skip
				if t&(1<<j) > 0 || trees[t|(1<<j)] {
					continue
				}

				candidate := false

				// loop over all edge nodes in this group, and
				// verify if node `j` would extend the tree, and
				// it's not violating any of the rules
				for i := 0; i < n; i++ {
					// self, or already in the subtree, or can't form
					// a new node
					if i == j || t&(1<<i) == 0 {
						continue
					}

					// outside the group, can't add
					if dist[i][j] > d {
						candidate = false
						break
					}

					// the node can extend the current subtree, add
					// as a candidate
					if dist[i][j] == d {
						candidate = true
					}
				}

				// the node can extend, and the new subtree hasn't been
				// seen before
				if candidate {
					trees[t|(1<<j)] = true
					subTrees[d-1] = append(subTrees[d-1], t|(1<<j))
				}
			}
		}

		ans[d-1] = len(subTrees[d-1])
	}

	fmt.Println(subTrees)

	return ans
}

func populateDistGrid(dist [][]int, edges map[int][]int, base, n int) {
	stack := edges[base]
	d := 2
	visited := 1 << base

	for len(stack) > 0 {
		next := make([]int, 0, n)

		for _, node := range stack {
			visited |= 1 << node

			for _, n := range edges[node] {
				if visited&(1<<n) > 0 || dist[base][n] > 0 || n == base {
					continue
				}

				if dist[base][n] == 0 {
					dist[base][n] = d
					dist[n][base] = d
					next = append(next, n)
				}
			}
		}

		stack = next
		d++
	}
}
