package support

// IntHeap ...
type IntHeap struct {
	slice    []int
	max      bool
	heapSize int
}

// BuildHeap ...
func BuildHeap(slice []int, max bool) *IntHeap {
	h := &IntHeap{
		slice:    slice,
		max:      max,
		heapSize: len(slice),
	}

	for i := h.heapSize / 2; i >= 0; i-- {
		h.Heapify(i)
	}

	return h
}

// Heapify ...
func (h *IntHeap) Heapify(i int) {
	l, r := 2*i+1, 2*i+2
	pos := i

	if l < h.heapSize && ((h.max && h.slice[l] > h.slice[pos]) || (!h.max && h.slice[l] < h.slice[pos])) {
		pos = l
	}

	if r < h.heapSize && ((h.max && h.slice[r] > h.slice[pos]) || (!h.max && h.slice[r] < h.slice[pos])) {
		pos = r
	}

	// fmt.Println(i, pos, h.slice[i], h.slice[pos])

	if pos != i {
		h.slice[i], h.slice[pos] = h.slice[pos], h.slice[i]
		h.Heapify(pos)
	}
}

// Size ...
func (h *IntHeap) Size() int {
	return h.heapSize
}

// Push ...
func (h *IntHeap) Push(val int) {
	// insert the value to the heap tail
	h.slice = append(h.slice, val)
	h.heapSize++

	// move the value in position
	h.slice[0], h.slice[h.heapSize-1] = h.slice[h.heapSize-1], h.slice[0]

	// keep the heap in right shape
	h.Heapify(0)
}

// Pop ...
func (h *IntHeap) Pop() int {
	// move the value out of the position
	h.slice[0], h.slice[h.heapSize-1] = h.slice[h.heapSize-1], h.slice[0]
	val := h.slice[h.heapSize-1]

	// remove the tail value
	h.slice = h.slice[:h.heapSize-1]
	h.heapSize--

	// keep the heap in right shape
	h.Heapify(0)

	return val
}

// HeapSort ...
func HeapSort(slice []int, max bool) []int {
	h := BuildHeap(slice, max)

	for i := h.heapSize - 1; i >= 1; i-- {
		// move the value to the tail and exclude it -- it's in sorted format
		h.slice[0], h.slice[i] = h.slice[i], h.slice[0]
		h.heapSize--

		// maintain the heap structure for the remainder
		h.Heapify(0)
	}

	return h.slice
}
