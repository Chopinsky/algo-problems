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
	size := len(p.data)

	parents := make([][]int, size+1)
	dualParentsNode := 0

	for _, pair := range p.data {
		p, c := pair[0], pair[1]

		if len(parents[c]) > 0 {
			if dualParentsNode != 0 || len(parents[c]) > 1 {
				fmt.Println("[Exception] more than 1 node has dual parents:", c, "and", dualParentsNode)
			}

			// this is the epic center, nuke it!
			dualParentsNode = c
		} else if !verify(parents, p, c) {
			return pair
		}

		parents[c] = append(parents[c], p)
	}

	if dualParentsNode > 0 {
		return findRealRoot(parents, dualParentsNode)
	}

	return nil
}

func findRealRoot(parents [][]int, start int) []int {
	next := parents[start][1]
	visited := map[int]bool{
		start: true,
	}

	for !visited[next] {
		visited[next] = true

		if len(parents[next]) == 0 {
			// we find the root of this branch --> the true root, so the other parent shall be removed
			return []int{parents[start][0], start}
		}

		// fetch the grandparent
		next = parents[next][0]
	}

	// we've found a cycled directed graph, this is the one to eliminate
	return []int{parents[start][1], start}
}

func verify(parents [][]int, parent, child int) bool {
	for len(parents[parent]) > 0 {
		parent = parents[parent][0]

		// create the p -> c link will cause a cycle in the graph
		if parent == child {
			return false
		}
	}

	// we've reached a root
	return true
}
