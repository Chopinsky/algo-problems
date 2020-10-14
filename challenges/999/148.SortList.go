package challenges

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func sortList(head *ListNode) *ListNode {
	return mergeSort(head)
}

func mergeSort(h *ListNode) *ListNode {
	if h == nil || h.Next == nil {
		return h
	}

	s, f, last := h, h, h

	for f != nil {
		last = s
		s = s.Next
		f = f.Next

		if f != nil {
			f = f.Next
		}
	}

	// fmt.Println(*h, *s, *last)

	last.Next = nil
	l := mergeSort(h)
	r := mergeSort(s)

	return mergeList(l, r)
}

func mergeList(l, r *ListNode) *ListNode {
	if l == nil {
		return r
	}

	if r == nil {
		return l
	}

	var curr, head, node *ListNode

	for l != nil || r != nil {
		if l == nil {
			curr.Next = r
			break
		}

		if r == nil {
			curr.Next = l
			break
		}

		if l.Val < r.Val {
			node = l
			l = l.Next
		} else {
			node = r
			r = r.Next
		}

		if curr == nil {
			head = node
			curr = node
		} else {
			curr.Next = node
			curr = curr.Next
		}
	}

	return head
}
