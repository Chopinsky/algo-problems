package challenges

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers2(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}

	if l2 == nil {
		return l1
	}

	s1, s2 := stackify(l1, make([]*ListNode, 0, 128)), stackify(l2, make([]*ListNode, 0, 128))
	if len(s1) < len(s2) {
		s1, s2 = s2, s1
	}

	// fmt.Println(s1, s2)

	extra := 0
	p1, p2 := len(s1)-1, len(s2)-1

	for p1 >= 0 {
		s1[p1].Val += extra

		if p2 >= 0 {
			s1[p1].Val += s2[p2].Val
		}

		if s1[p1].Val >= 10 {
			s1[p1].Val -= 10
			extra = 1
		} else {
			extra = 0
		}

		p1--
		p2--
	}

	if extra == 1 {
		head := &ListNode{
			Val:  1,
			Next: s1[0],
		}

		return head
	}

	return s1[0]
}

func stackify(l *ListNode, s []*ListNode) []*ListNode {
	for l != nil {
		s = append(s, l)
		l = l.Next
	}

	return s
}
