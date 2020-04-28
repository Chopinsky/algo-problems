package shared

import (
	"container/heap"
)

// Compare ...
type Compare interface {
	Less(another Compare) bool
}

// An Item is something we manage in a priority queue.
type Item struct {
	value Compare // The value of the item; arbitrary.
	index int     // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

// PriorityQueueInit ...
func PriorityQueueInit(size int) PriorityQueue {
	pq := make(PriorityQueue, 0, size)
	heap.Init(&pq)

	return pq
}

func (pq PriorityQueue) Len() int {
	return len(pq)
}

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	return pq[i].value.Less(pq[j].value)
}

// Swap ...
func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

// Push ...
func (pq *PriorityQueue) Push(val interface{}) {
	n := len(*pq)

	item := &Item{
		value: val.(Compare),
		index: n,
	}

	*pq = append(*pq, item)
	heap.Fix(pq, item.index)
}

// Pop ...
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)

	item := old[0]
	item.index = -1 // for safety

	old[0] = old[n-1]
	old[0].index = 0
	old[n-1] = nil  // avoid memory leak

	*pq = old[:n-1]
	heap.Fix(pq, 0)

	return item.value
}

// Update modifies the priority and value of an Item in the queue.
func (pq *PriorityQueue) Update(item *Item, value Compare) {
	item.value = value
	heap.Fix(pq, item.index)
}
