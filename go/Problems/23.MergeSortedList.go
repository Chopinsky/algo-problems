package problems

import (
	"fmt"

	d "../Utils"
)

// MSL ...
type MSL struct {
	source    []*listNode
	output    *listNode
	testCount int
}

// CreateMSL ...
func CreateMSL() *MSL {
	return &MSL{}
}

// Build ...
func (p *MSL) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	var src [][]int
	var output []int

	switch test {
	default:
		src = [][]int{
			{1, 4, 5},
			{1, 3, 4},
			{2, 6},
		}

		output = []int{1, 1, 2, 3, 4, 4, 5, 6}

	}

	p.source = make([]*listNode, len(src))
	for i := range src {
		head := buildList(src[i])
		p.source[i] = head
	}

	p.output = buildList(output)
}

// ResetGlobals ...
func (p *MSL) ResetGlobals() {
}

// Run ...
func (p *MSL) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			fmt.Println("\nTest Case -", i, ":")

			h := p.buildHeap()
			fmt.Print("Calculated result: ")
			p.merge(h).output()
			fmt.Println()

			fmt.Print("Expected result:   ")
			p.output.output()
			fmt.Println()
		}

		fmt.Println()
	}
}

func (p *MSL) buildHeap() *d.Heap {
	ary := make([]int, len(p.source))
	for i := range p.source {
		ary[i] = p.source[i].val
	}

	h := d.NewHeap(ary, true)

	return h
}

func (p *MSL) merge(heap *d.Heap) *listNode {
	if len(p.source) == 1 {
		return p.source[0]
	}

	if heap.IsEmpty() {
		return nil
	}

	var upperBound int
	var nextRoot *d.HeapNode
	var next *listNode

	root := heap.Peek()
	idx := root.GetData()
	head, tail := p.source[idx], p.source[idx]

	for !heap.IsEmpty() {
		nextRoot = heap.PeekNextRoot()
		if nextRoot != nil {
			upperBound = nextRoot.GetVal()
		} else {
			heap.Pop()
			break
		}

		for {
			next = tail.next

			if next != nil {
				if next.val <= upperBound {
					tail = next
				} else {
					p.source[idx] = next
					heap.UpdateRoot(next.val)
					break
				}
			} else {
				heap.Pop()
				p.source[idx] = nil
				break
			}
		}

		// we're done with this list, get the next list
		root = heap.Peek()
		if root == nil {
			break
		}

		idx = root.GetData()
		tail.next = p.source[idx]

		if tail.next != nil {
			tail = tail.next
		} else {
			break
		}
	}

	last := heap.Pop()
	if last != nil {
		tail.next = p.source[last.GetData()]
	}

	return head
}

type listNode struct {
	val  int
	next *listNode
}

func buildList(src []int) *listNode {
	head := &listNode{
		val:  src[0],
		next: nil,
	}

	var next, last *listNode
	last = head

	for i := 1; i < len(src); i++ {
		next = &listNode{
			val:  src[i],
			next: nil,
		}

		last.next = next
		last = next
	}

	return head
}

func (n *listNode) output() {
	head, link := n, " -> "
	for head != nil {
		if head.next == nil {
			link = ""
		}

		fmt.Print(head.val, link)
		head = head.next
	}
}
