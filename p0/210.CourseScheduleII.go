package p0

import (
	"container/heap"
	"fmt"
	"time"

	s "go-problems/shared"
)

// CSIIProblems ...
type CSIIProblems struct {
	set []*CSII
}

// Solve ...
func (p *CSIIProblems) Solve() {
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

// CSII ...
type CSII struct {
	data   [][]int
	n      int
	output int
}

// CreateCSII ...
func CreateCSII() s.Problem {
	set := make([]*CSII, 0, 4)

	set = append(set, &CSII{
		data:   [][]int{
			{1,0}, {2,0}, {3,1}, {3,2},
		},
		n: 4,
		output: 0,
	})

	return &CSIIProblems{set}
}

func (p *CSII) solve() []int {
	return findOrder(p.n, p.data)
}

func findOrder(numCourses int, prerequisites [][]int) []int {
  if numCourses == 0 || prerequisites == nil {
    return []int{}
  }

  courses := make([]*Node, numCourses)
  for i := range courses {
    courses[i] = &Node {
      c:   i,
      inc: 0,
      out: []int{},
    }
  }

  h := make(Queue, 0, numCourses)
  // taken := make([]int, numCourses)

  for _, edge := range prerequisites {
    a, b := edge[0], edge[1]
    if a == b {
      return []int{}
    }

    na, nb := courses[a], courses[b]

    if na != nil {
      na.inc++
    }

    if nb != nil {
      nb.out = append(nb.out, a)
    }
  }

  for i := range courses {
    fmt.Println(courses[i])
  }

  for _, n := range courses {
    if n.inc == 0 {
      h.Push(n)
    }
  }

  res := make([]int, 0, numCourses)
  for h.Len() > 0 {
    n := h.Pop().(*Node)
    courses[n.c] = nil

    // fmt.Println("pop:", n.c)

    for _, d := range n.out {
      next := courses[d]
      if next == nil {
        continue
      }

      next.inc--
      if next.inc == 0 {
        h.Push(next)
      }
    }

    res = append(res, n.c)
  }

  for i := range courses {
    if courses[i] == nil {
      continue
    }

    if courses[i].inc != 0 {
      return []int{}
    }

    res = append(res, courses[i].c)
  }

  return res
}

// Queue ...
type Queue []*Node

// Node ...
type Node struct {
  c int
  inc int
  out []int
}

// Len ...
func (q Queue) Len() int {
  return len(q)
}

// Less ...
func (q Queue) Less(i, j int) bool {
  return len(q[i].out) > len(q[j].out)
}

// Swap ...
func (q Queue) Swap(i, j int) {
  q[i], q[j] = q[j], q[i]
}

// Push ...
func (q *Queue) Push(val interface{}) {
  v := val.(*Node)
  *q = append(*q, v)
  heap.Fix(q, q.Len()-1)
}

// Pop ...
func (q *Queue) Pop() interface{} {
  old := *q
  n := old.Len()
  item := old[0]

  old.Swap(0, n-1)
  *q = old[:n-1]
  heap.Fix(q, 0)

  return item
}
