package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// TSProblems ...
type TSProblems struct {
	set []*TS
}

// Solve ...
func (p *TSProblems) Solve() {
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

// TS ...
type TS struct {
	data   []byte
	n      int
	output int
}

// CreateTS ...
func CreateTS() s.Problem {
	set := make([]*TS, 0, 4)

	set = append(set, &TS{
		data:   []byte{'A','A','A','A','A','A','B','C','D','E','F','G'},
		n:      2,
		output: 16,
	})

	return &TSProblems{set}
}

func (p *TS) solve() int {
	return leastInterval(p.data, p.n)
}

func leastInterval(t []byte, n int) int {
  if t == nil || len(t) == 0 {
    return 0
  }

  if n == 0 {
    return len(t)
  }

  tasks := make([]int, 26)

  // max -- the max count of jobs for any task in the queue
  // maxCount -- the number of tasks that has `max` jobs in the queue
  var max, maxCount int

  for i := range t {
    val := int(t[i] - byte('A'))
    tasks[val]++

    if max == tasks[val] {
      maxCount++
    } else if (max < tasks[val]) {
      max = tasks[val]
      maxCount = 1
    }
  }

  // fmt.Println(tasks)

  // number of parts to fill other jobs in, i.e. `A _ _ | A _ _ | A`
  // gives 2 parts
  partCount := max - 1

  // the remainder slots left in each part for less frequent jobs,
  // i.e. `A B _ _ | A B _ _ | AB ` has 2 slots for each part
  partLen := n - (maxCount - 1)

  // total count of empty slots to fill with the tasks
  emptySlots := partCount * partLen

  // the count of the less frequent jobs not yet filled in
  remTasks := len(t) - max *maxCount

  // the slots left for idle, since no other jobs can be scheduled there
  idles := emptySlots - remTasks

  if idles < 0 {
    idles = 0
  }

  return len(t) + idles
}
