package utils

import (
	"fmt"
)

// Node ...
type Node struct {
	val  int
	next *Node
}

// Build ...
func Build(arr []int) *Node {
	var head, last *Node

	for i := range arr {
		curr := Node{
			val:  arr[i],
			next: nil,
		}

		if i == 0 {
			head = &curr
		}

		if last != nil {
			last.next = &curr
		}

		last = &curr
	}

	return head
}

// Next ...
func (n *Node) Next() *Node {
	return n.next
}

// Value ...
func (n *Node) Value() int {
	return n.val
}

// DebugList ...
func DebugList(head *Node) {
	curr := head
	fmt.Println()

	for {
		fmt.Println("Current node value: ", curr.val, "; Has next node: ", curr.next == nil)
		if curr.next == nil {
			break
		}

		curr = curr.next
	}
}
