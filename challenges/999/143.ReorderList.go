package challenges

import (
	"fmt"
)

// ListNode ...
type ListNode struct {
	Val  int
	Next *ListNode
}

func reorderList(head *ListNode) {
	if head == nil || head.Next == nil || head.Next.Next == nil {
		return
	}

	s, f := head, head

	for f.Next != nil {
		s = s.Next
		f = f.Next

		if f.Next != nil {
			f = f.Next
		}
	}

	fmt.Println("f/s:", s.Val, f.Val)

	rh := reverseList(s.Next)
	h := head
	s.Next = nil

	for rh != nil && h != nil {
		fmt.Println("loop:", rh.Val, h.Val)

		ch := h
		crh := rh

		h = h.Next
		rh = rh.Next

		ch.Next = crh
		crh.Next = h
	}

	fmt.Println("done ... ")
}

func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	last := head
	next := head.Next
	last.Next = nil

	for next != nil {
		cn := next
		next = next.Next

		cn.Next = last
		last = cn
	}

	return last
}
