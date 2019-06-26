package problems

import (
	"fmt"

	d "../Utils"
)

// MSL ...
type MSL struct {
	source    []*listNode
	output    []int
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

	switch test {
	default:
		src = [][]int{
			{1, 4, 5},
			{1, 3, 4},
			{2, 6},
		}

		p.output = []int{1, 1, 2, 3, 4, 4, 5, 6}

	}

	p.source = make([]*listNode, len(src))
	for i := range src {
		head := buildList(src[i])
		p.source[i] = head
	}
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

			//TODO: write code here ...

			fmt.Println("\nTest case: ", i, ":")
			// d.Output(result, p.output)
		}

		fmt.Println()
	}

	d.TestHeap()
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
