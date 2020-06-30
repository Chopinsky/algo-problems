package p1

import (
	"container/heap"
	"fmt"
	"time"

	s "go-problems/shared"
)

// PCIIProblems ...
type PCIIProblems struct {
	set []*PCII
}

// Solve ...
func (p *PCIIProblems) Solve() {
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

// PCII ...
type PCII struct {
	data   [][]int
	n      int
	k      int
	output int
}

// CreatePCII ...
func CreatePCII() s.Problem {
	set := make([]*PCII, 0, 4)

	set = append(set, &PCII{
		data: [][]int{
			{2, 1}, {3, 1}, {1, 4},
		},
		n:      4,
		k:      2,
		output: 3,
	})

	set = append(set, &PCII{
		data: [][]int{
			{2, 1}, {3, 1}, {4, 1}, {1, 5},
		},
		n:      5,
		k:      2,
		output: 4,
	})

	return &PCIIProblems{set}
}

func (p *PCII) solve() int {
	n, k, d := p.n, p.k, p.data
	g := makeGraph(n, d)
	h := make(vtxHeap, 0, n)

	// init the heap with courses that have no dependencies
	for _, v := range g {
		if v.incoming == 0 {
			h = append(h, v)
		}
	}

	heap.Init(&h)

	taken, sem := 0, 0
	pending := make([]*vertex, 0, n)

	for taken < n {
		curr := 0

		for i := range pending {
			heap.Push(&h, pending[i])
		}

		if len(pending) > 0 {
			pending = pending[len(pending):]
		}

		for h.Len() > 0 && curr < k {
			v := heap.Pop(&h).(*vertex)
			curr++
			taken++

			for _, next := range v.outgoing {
				g[next].incoming--
				if g[next].incoming == 0 {
					pending = append(pending, g[next])
				}
			}
		}

		sem++
	}

	return sem
}

type vtxHeap []*vertex

type vertex struct {
	outgoing []int
	incoming int
}

func (h vtxHeap) Len() int {
	return len(h)
}

func (h vtxHeap) Less(i, j int) bool {
	return len(h[i].outgoing) > len(h[j].outgoing)
}

func (h vtxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *vtxHeap) Push(x interface{}) {
	v := x.(*vertex)
	v.incoming = h.Len()
	*h = append(*h, v)
}

func (h *vtxHeap) Pop() interface{} {
	old := *h
	n := old.Len()

	v := old[n-1]
	old[n-1] = nil

	*h = old[:n-1]
	return v
}

func makeGraph(n int, d [][]int) map[int]*vertex {
	g := make(map[int]*vertex)

	for i := 0; i < n; i++ {
		g[i] = &vertex{
			outgoing: make([]int, 0, n),
			incoming: 0,
		}
	}

	for i := range d {
		u, v := d[i][0]-1, d[i][1]-1
		g[u].outgoing = append(g[u].outgoing, v)
		g[v].incoming++
	}

	return g
}
