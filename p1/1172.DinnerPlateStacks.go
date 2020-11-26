package p1

import (
	"container/heap"
	"fmt"
	"time"

	s "go-problems/shared"
)

// DPSProblems ...
type DPSProblems struct {
	set []*DPS
}

// Solve ...
func (p *DPSProblems) Solve() {
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

// DPS ...
type DPS struct {
	data   []string
	input  [][]int
	output []int
}

// CreateDPS ...
func CreateDPS() s.Problem {
	set := make([]*DPS, 0, 4)

	set = append(set, &DPS{
		data: []string{"DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"},
		input: [][]int{
			{2}, {1}, {2}, {3}, {4}, {5}, {0}, {20}, {21}, {0}, {2}, {}, {}, {}, {}, {},
		},
		output: []int{
			0, 0, 0, 0, 0, 0, 2, 0, 0, 20, 21, 5, 4, 3, 1, -1,
		},
	})

	return &DPSProblems{set}
}

func (p *DPS) solve() int {
	return 0
}

// DinnerPlates ...
type DinnerPlates struct {
	capacity int
	stack    [][]int
	h        Queue
}

// Queue ...
type Queue []int

// Len ...
func (q Queue) Len() int {
	return len(q)
}

// Less ...
func (q Queue) Less(i, j int) bool {
	return q[i] < q[j]
}

// Swap ...
func (q Queue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}

// Push ...
func (q *Queue) Push(val interface{}) {
	v := val.(int)
	*q = append(*q, v)
	heap.Fix(q, q.Len()-1)
}

// Pop ...
func (q *Queue) Pop() interface{} {
	old := *q
	n := old.Len()
	pos := old[0]

	old.Swap(0, n-1)
	*q = old[:n-1]

	heap.Fix(q, 0)
	return pos
}

func dpConstructor(capacity int) DinnerPlates {
	return DinnerPlates{
		capacity: capacity,
		stack:    [][]int{},
		h:        make(Queue, 0, capacity),
	}
}

// Push ...
func (t *DinnerPlates) Push(val int) {
	pos := -1
	last := len(t.stack) - 1
	var head, size int

	for t.h.Len() > 0 {
		head = t.h[0]
		if head > last {
			t.h.Pop()
			continue
		}

		size = len(t.stack[head])

		if size < t.capacity {
			pos = head
			if size+1 == t.capacity {
				t.h.Pop()
			}

			break
		}

		t.h.Pop()
	}

	if pos == -1 {
		t.stack = append(t.stack, []int{val})

		if t.capacity > 1 {
			t.h.Push(len(t.stack) - 1)
		}
	} else {
		t.stack[pos] = append(t.stack[pos], val)
	}
}

// Pop ...
func (t *DinnerPlates) Pop() int {
	last := len(t.stack) - 1

	// fmt.Println(t.stack)

	for last >= 0 {
		size := len(t.stack[last])

		if size == 0 {
			t.stack = t.stack[:last]
			last--
			continue
		}

		val := t.stack[last][size-1]

		if size == 1 {
			// remove t stack since it's empty
			t.stack = t.stack[:last]
			last--
		} else {
			t.stack[last] = t.stack[last][:size-1]

			// now it can take new plates
			if size == t.capacity {
				t.h.Push(last)
			}
		}

		pos := -1
		for i := t.h.Len() - 1; i >= 0; i-- {
			if t.h[i] > last {
				pos = i
			}
		}

		if pos >= 0 {
			t.h = t.h[:pos]
		}

		return val
	}

	return -1
}

// PopAtStack ...
func (t *DinnerPlates) PopAtStack(index int) int {
	if index >= len(t.stack) {
		return -1
	}

	size := len(t.stack[index])
	if size == 0 {
		return -1
	}

	val := t.stack[index][size-1]

	if size == 1 && index == len(t.stack)-1 {
		// remove t stack since it's the last one and empty
		t.stack = t.stack[:index]
		index--

		pos := -1
		for i := t.h.Len() - 1; i >= 0; i-- {
			if t.h[i] > index {
				pos = i
			}
		}

		if pos >= 0 {
			t.h = t.h[:pos]
		}
	} else {
		t.stack[index] = t.stack[index][:size-1]

		// now it can take new plates
		if size == t.capacity {
			t.h.Push(index)
		}
	}

	// fmt.Println("post pop at stack", index, t.stack, t.h)

	return val
}
