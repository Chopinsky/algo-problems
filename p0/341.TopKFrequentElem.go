package p0

import (
	"container/heap"
	"fmt"
	"time"

	s "go-problems/shared"
)

// TKFEProblems ...
type TKFEProblems struct {
	set []*TKFE
}

// Solve ...
func (p *TKFEProblems) Solve() {
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

// TKFE ...
type TKFE struct {
	data   []int
	k      int
	output int
}

// CreateTKFE ...
func CreateTKFE() s.Problem {
	set := make([]*TKFE, 0, 4)

	set = append(set, &TKFE{
		data:   []int{},
		output: 0,
	})

	return &TKFEProblems{set}
}

func (p *TKFE) solve() []int {
	return topKFrequent(p.data, p.k)
}

func topKFrequent(nums []int, k int) []int {
  m := make(map[int]int, len(nums))
  h := make(pq, 0, k)
  hm := make(map[int]*node, k)

  for i := range nums {
    val := nums[i]
    next := m[val] + 1

    if n, ok := hm[val]; ok {
      // the node already exists in the heap, update the node
      // and fix the heap if needed
      n.count++

      if h.Len() == k {
        heap.Fix(&h, n.pos)
      }
    } else if h.Len() < k {
      // not hitting the limit, keep adding
      n := &node{
        num: val,
        count: 1,
        pos: -1,
      }

      h.Push(n)
      hm[val] = n

      // now we have the full house, heapify it
      if h.Len() == k {
        heap.Init(&h)
        // fmt.Println("init @", i, val)
      }
    } else {
      pop, n := h.Update(val, next)

      if n != nil {
        delete(hm, pop)
        hm[val] = n
      }

      // fmt.Println("pop @", i, val, pop, n)
    }

    m[val] = next
  }

  res := make([]int, 0, h.Len())
  for i := range h {
    res = append(res, h[i].num)
  }

  return res
}

type pq []*node

type node struct {
	num int
	count int
  pos int
}

func (h pq) Len() int {
	return len(h)
}

func (h pq) Less(i, j int) bool {
	return h[i].count < h[j].count
}

func (h pq) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
  h[i].pos, h[j].pos = h[j].pos, h[i].pos
}

func (h *pq) Update(n, c int) (int, *node) {
  if (*h)[0].count >= c {
    return -1, nil
  }

  oldVal := (*h)[0].num
  (*h)[0].num = n
  (*h)[0].count = c
  node := (*h)[0]

  heap.Fix(h, 0)

  return oldVal, node
}

func (h *pq) Push(x interface{}) {
	v := x.(*node)
  v.pos = h.Len()
	*h = append(*h, v)
}

func (h *pq) Pop() interface{} {
	old := *h
	n := old.Len()

	v := old[n-1]
	old[n-1] = nil

	*h = old[:n-1]

	return v
}