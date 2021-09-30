package challenges

import (
	"container/heap"
	"sort"
)

func carPooling(trips [][]int, capacity int) bool {
	sort.Slice(trips, func(i, j int) bool {
		if trips[i][1] == trips[j][1] {
			if trips[i][2] == trips[j][2] {
				return trips[i][0] > trips[j][0]
			}

			return trips[i][2] < trips[j][2]
		}

		return trips[i][1] < trips[j][1]
	})

	// fmt.Println(trips)

	q := make(queue, 0, len(trips))
	q.Push(trips[0])

	c := trips[0][0]
	if c > capacity {
		return false
	}

	var milestone int
	var top []int

	for i := 1; i < len(trips); i++ {
		if q.Len() == 0 {
			c += trips[i][0]
			q.Push(trips[i])
			continue
		}

		milestone = trips[i][1]
		top = q[0]

		for top != nil && top[2] <= milestone {
			c -= top[0]
			q.Pop()

			if q.Len() > 0 {
				top = q[0]
			} else {
				top = nil
			}
		}

		c += trips[i][0]
		if c > capacity {
			return false
		}

		q.Push(trips[i])
	}

	return true
}

type queue [][]int

func (q queue) Len() int {
	return len(q)
}

func (q queue) Less(i, j int) bool {
	if q[i][2] == q[j][2] {
		return q[i][0] > q[j][0]
	}

	return q[i][2] < q[j][2]
}

func (q queue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}

func (q *queue) Push(x interface{}) {
	item := x.([]int)
	*q = append(*q, item)
	heap.Fix(q, q.Len()-1)
}

func (q *queue) Pop() interface{} {
	old := *q

	n := len(old)
	item := old[0]

	q.Swap(0, n-1)
	old[n-1] = nil

	*q = old[:n-1]
	heap.Fix(q, 0)

	return item
}
