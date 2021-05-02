package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// NRPProblems ...
type NRPProblems struct {
	set []*NRP
}

// Solve ...
func (p *NRPProblems) Solve() {
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

// NRP ...
type NRP struct {
	edges  [][]int
	n      int
	output int
}

// CreateNRP ...
func CreateNRP() s.Problem {
	set := make([]*NRP, 0, 4)

	set = append(set, &NRP{
		edges: [][]int{
			{1, 2, 3},
			{1, 3, 3},
			{2, 3, 1},
			{1, 4, 2},
			{5, 2, 2},
			{3, 5, 1},
			{5, 4, 10},
		},
		n:      5,
		output: 3,
	})

	return &NRPProblems{set}
}

func (p *NRP) solve() int {
	e := make(map[int]map[int]int)

	for _, edge := range p.edges {
		x, y, d := edge[0]-1, edge[1]-1, edge[2]
		if e[x] == nil {
			e[x] = make(map[int]int)
		}

		if e[y] == nil {
			e[y] = make(map[int]int)
		}

		e[x][y] = d
		e[y][x] = d
	}

	// fmt.Println(e)

	last := p.n - 1
	dist := make([]int, p.n)
	nodes := make([]int, 0, p.n)
	next := make([]int, 0, p.n)

	// calc distances
	nodes = append(nodes, last)
	for len(nodes) > 0 {
		for _, node := range nodes {
			currDist := dist[node]

			for n, d := range e[node] {
				if (dist[n] == 0 && n != last) || currDist+d < dist[n] {
					dist[n] = currDist + d
					next = append(next, n)
				}
			}
		}

		nodes, next = next, nodes
		next = next[:0]
	}

	// fmt.Println(dist)

	paths := make([]int, p.n)
	paths[0] = 1

	q := make(IntsQueue, 0, p.n)
	q.Push([]int{0, 0})

	visited := make(map[int]bool)

	// calc paths
	for q.Len() > 0 {
		arr := q.Pop().([]int)
		curr := arr[1]
		if visited[curr] {
			continue
		}

		visited[curr] = true
		// fmt.Println(curr, arr, q)

		for node := range e[curr] {
			if dist[node] >= dist[curr] || visited[node] {
				continue
			}

			paths[node] += paths[curr]
			q.Push([]int{-dist[node], node})
		}

		nodes, next = next, nodes
		next = next[:0]
	}

	// fmt.Println(paths)

	return paths[p.n-1]
}
