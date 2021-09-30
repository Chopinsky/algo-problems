package challenges

import "container/heap"

func kthSmallest(mat [][]int, k int) int {
	q := make(IntQueue, 0, k)
	temp := make(IntQueue, 0, k*len(mat[0]))

	q.Push(0)

	// idea is to save k small sums from the first i rows, then
	// add 1 row, then recalculate the smallest k sums for the
	// previous selections plus a number from the new row, and
	// repeat until we reach the last row
	for _, r := range mat {
		for q.Len() > 0 {
			curr := q.Pop().(int)

			for _, val := range r {
				temp.Push(curr + val)
			}
		}

		// reset
		q = q[:0]

		// for next calc round, we only keep the first k sums
		for q.Len() < k && temp.Len() > 0 {
			q.Push(temp.Pop().(int))
		}

		// reset
		temp = temp[:0]
	}

	var last int
	for _, val := range q {
		if val >= last {
			last = val
		}
	}

	return last
}

// IntQueue ...
type IntQueue []int

// Len ...
func (q IntQueue) Len() int {
	return len(q)
}

// Less ...
func (q IntQueue) Less(i, j int) bool {
	return q[i] < q[j]
}

// Swap ...
func (q IntQueue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}

// Push ...
func (q *IntQueue) Push(val interface{}) {
	v := val.(int)
	*q = append(*q, v)
	heap.Fix(q, q.Len()-1)
}

// Pop ...
func (q *IntQueue) Pop() interface{} {
	old := *q
	n := old.Len()
	val := old[0]

	old.Swap(0, n-1)
	*q = old[:n-1]
	heap.Fix(q, 0)

	return val
}
