package shared

import (
	"container/heap"
	"fmt"
)

// IntHeap ...
type IntHeap [][]int

// IntHeapInit ...
func IntHeapInit(src []int) IntHeap {
	size := len(src)
	h := make(IntHeap, size)

	for i := range src {
		h[i] = []int{src[i], i}
	}

	heap.Init(&h)
	return h
}

// Heap ...
func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i][0] < h[j][0]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

// Push ...
func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.([]int))
	heap.Fix(h, h.Len()-1)
}

// Pop ...
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)

	x := old[0]
	old[0] = old[n-1]
	*h = old[0 : n-1]

	heap.Fix(h, 0)

	return x
}

// Heap ...
type Heap struct {
	slice    [][]int
	heapSize int
	records  map[int]int
}

// InitHeap ...
func InitHeap(size int) *Heap {
	h := &Heap{
		slice:    make([][]int, 0, size),
		heapSize: 0,
		records:  make(map[int]int, size),
	}

	return h
}

func (h *Heap) swap(i, j int) {
	h.slice[i], h.slice[j] = h.slice[j], h.slice[i]
	h.records[h.slice[i][0]] = i
	h.records[h.slice[j][0]] = j
}

// Heapify ...
func (h *Heap) Heapify(i int) {
	l, r := 2*i+1, 2*i+2
	pos := i

	if l < h.heapSize && h.slice[l][1] > h.slice[pos][1] {
		pos = l
	}

	if r < h.heapSize && h.slice[r][1] > h.slice[pos][1] {
		pos = r
	}

	// fmt.Println(i, pos, h.slice[i], h.slice[pos])

	if pos != i {
		h.swap(i, pos)
		h.Heapify(pos)
	}
}

// Size ...
func (h *Heap) Size() int {
	return h.heapSize
}

// Peek ...
func (h *Heap) Peek() []int {
	return h.slice[0]
}

// Push ...
func (h *Heap) Push(val []int) {
	// insert the value to the heap tail
	h.slice = append(h.slice, val)
	pos := h.heapSize

	h.records[val[0]] = pos
	h.heapSize++

	for pos > 0 {
		parent := pos / 2

		// fmt.Println("pushing:", h.slice)

		if h.slice[pos][1] < h.slice[parent][1] {
			break
		}

		h.swap(parent, pos)
		h.Heapify(parent)

		pos = parent
	}
}

// Pop ...
func (h *Heap) Pop() []int {
	// move the value out of the position
	h.slice[0], h.slice[h.heapSize-1] = h.slice[h.heapSize-1], h.slice[0]
	val := h.slice[h.heapSize-1]

	// remove the tail value
	h.slice[h.heapSize-1] = nil
	h.slice = h.slice[:h.heapSize-1]
	delete(h.records, val[0])

	h.heapSize--

	// keep the heap in right shape
	h.Heapify(0)

	return val
}

// Update ...
func (h *Heap) Update(idx int, val []int) {
	pos, ok := h.records[idx]

	if !ok {
		h.Push(val)
		return
	}

	delete(h.records, idx)

	h.slice[pos] = val
	h.records[val[0]] = pos

	// fix upstream
	for pos > 0 {
		parent := pos / 2
		if h.slice[pos][0] < h.slice[parent][0] {
			break
		}

		h.swap(parent, pos)
		pos = parent
	}

	// fix downstream
	h.Heapify(pos)
}

// Debug ...
func (h *Heap) Debug() {
	fmt.Println(h.slice)
}
