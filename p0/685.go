package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

var round = 1

// RCIIProblems ...
type RCIIProblems struct {
	set []*RCII
}

// Solve ...
func (p *RCIIProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= round; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == round {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm took", time.Since(start))
}

// RCII ...
type RCII struct {
	data   [][]int
	output []int
}

// CreateRCII ...
func CreateRCII() s.Problem {
	set := make([]*RCII, 0, 4)

	set = append(set, &RCII{
		data:   [][]int{{1, 2}, {1, 3}, {2, 3}},
		output: []int{2, 3},
	})

	set = append(set, &RCII{
		data:   [][]int{{1, 2}, {2, 3}, {3, 4}, {4, 1}, {1, 5}},
		output: []int{4, 1},
	})

	set = append(set, &RCII{
		data:   [][]int{{1, 2}, {2, 3}, {3, 4}, {4, 1}, {5, 1}},
		output: []int{4, 1},
	})

	set = append(set, &RCII{
		data:   [][]int{{2, 3}, {3, 4}, {4, 1}, {5, 1}, {1, 2}},
		output: []int{1, 2},
	})

	return &RCIIProblems{set}
}

func (p *RCII) solve() []int {
	return findRedundantDirectedConnection(p.data)
}

func findRedundantDirectedConnection(edges [][]int) []int {
	size := len(edges)
	root := -1

	hasParent := make([]bool, size+1)
	m := make(map[int]int)
	conflict := []int{-1, -1, -1}

	for i, e := range edges {
		v := e[1]
		hasParent[v] = true

		if j, ok := m[v]; ok {
			// found the dual-parent conflict: v
			conflict[0] = v

			// duplicate edges: i and j
			conflict[1] = j
			conflict[2] = i
		} else {
			m[v] = i
		}
	}

	// fmt.Println(hasParent)

	for i := range hasParent {
		if i == 0 {
			continue
		}

		if !hasParent[i] {
			root = i
			break
		}
	}

	// the real root is in a circle! use union-find to remove the
	// edge added later to form the circle!
	if root == -1 || conflict[0] == -1 {
		u := make([]int, size)
		for i := range u {
			u[i] = i
		}

		for _, e := range edges {
			if !union(u, e[0]-1, e[1]-1) {
				return e
			}
		}

		// shouldn't happen
		return nil
	}

	// fmt.Println(root, conflict[0], edges[conflict[1]], edges[conflict[2]])

	pathA := backtrace(m, edges, edges[conflict[1]][0], conflict[0], root)
	if !pathA {
		return edges[conflict[1]]
	}

	return edges[conflict[2]]
}

func backtrace(m map[int]int, edges [][]int, node, conflict, root int) bool {
	for node != root {
		p := edges[m[node]][0]
		if p == conflict {
			return false
		}

		node = p
	}

	return true
}

func union(u []int, p, c int) bool {
	rp, rc := findRCII(u, p), findRCII(u, c)

	if rc == rp {
		fmt.Println("last:", p+1, c+1, rc)
		return false
	}

	u[rc] = rp
	return true
}

func findRCII(u []int, s int) int {
	// todo: will need to tweek this function

	for u[s] != s {
		s = u[s]
	}

	return s
}
