package utils

import "fmt"

// Heap ...
type Heap struct {
	inner  []*HeapNode
	minify bool
}

// HeapNode ...
type HeapNode struct {
	val  int
	data int
}

// NewNode ..
func NewNode(val, data int) *HeapNode {
	return &HeapNode{
		val:  val,
		data: data,
	}
}

// GetVal ...
func (n *HeapNode) GetVal() int {
	return n.val
}

// GetData ...
func (n *HeapNode) GetData() int {
	return n.data
}

// NewHeap ...
func NewHeap(src []int, minify bool) *Heap {
	h := &Heap{
		inner:  make([]*HeapNode, len(src)),
		minify: minify,
	}

	for i := range src {
		h.inner[i] = &HeapNode{
			val:  src[i],
			data: i,
		}
	}

	h.Heapify()

	return h
}

// ToggleMinify ...
func (h *Heap) ToggleMinify(minify bool) {
	if minify == h.minify {
		return
	}

	h.minify = minify
	h.Heapify()
}

// Heapify ...
func (h *Heap) Heapify() {
	n := len(h.inner)
	for i := n/2 - 1; i >= 0; i-- {
		h.siftDown(i)
	}
}

// Push ...
func (h *Heap) Push(val, data int) {
	node := &HeapNode{
		val:  val,
		data: data,
	}

	h.inner = append(h.inner, node)
	idx, parent := len(h.inner)-1, 0

	// Now sift-up the heap
	for idx > 0 {
		parent = (idx - 1) / 2

		if h.shallSwap(idx, parent) {
			h.inner[idx], h.inner[parent] = h.inner[parent], h.inner[idx]
		}

		idx = parent
	}
}

// Pop ...
func (h *Heap) Pop() *HeapNode {
	return h.Remove(0)
}

// Remove ...
func (h *Heap) Remove(idx int) *HeapNode {
	n := len(h.inner)
	if idx >= n {
		return nil
	}

	h.inner[n-1], h.inner[idx] = h.inner[idx], h.inner[n-1]
	res := h.inner[n-1]

	h.inner, h.inner[n-1] = h.inner[:n-1], nil
	h.siftDown(idx)

	return res
}

// RemoveData ...
func (h *Heap) RemoveData(data int) *HeapNode {
	for i := range h.inner {
		if h.inner[i].data == data {
			return h.Remove(i)
		}
	}

	return nil
}

// Peek ...
func (h *Heap) Peek() *HeapNode {
	return h.inner[0]
}

// IsEmpty ...
func (h *Heap) IsEmpty() bool {
	return len(h.inner) == 0
}

func (h *Heap) siftDown(idx int) {
	bound := len(h.inner)
	if idx > bound/2-1 {
		return
	}

	left, right, next := 2*idx+1, 2*idx+2, idx

	if left < bound && h.shallSwap(left, next) {
		next = left
	}

	if right < bound && h.shallSwap(right, next) {
		next = right
	}

	if next != idx {
		h.inner[idx], h.inner[next] = h.inner[next], h.inner[idx]
		if next <= bound/2-1 {
			h.siftDown(next)
		}
	}
}

func (h *Heap) shallSwap(child, parent int) bool {
	n := len(h.inner)
	if child >= n || parent >= n {
		return false
	}

	if h.minify {
		return h.inner[child].val < h.inner[parent].val
	}

	return h.inner[child].val > h.inner[parent].val
}

// TestHeap ...
func TestHeap() {
	src := []int{7, 8, 11, 9, 1, 14, 10, 1, 4, 2, 4, 2, 5, 6}

	h := NewHeap(src, true)
	h.Push(3, 0)

	for !h.IsEmpty() {
		node := h.Pop()
		fmt.Println(node.GetVal())
	}

	fmt.Println("++++++++++++++++++++")

	h = NewHeap(src, false)
	h.Push(3, 0)

	for !h.IsEmpty() {
		node := h.Pop()
		fmt.Println(node.GetVal())
	}
}
