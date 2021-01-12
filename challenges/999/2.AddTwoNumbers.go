package challenges

/**
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
*/
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}

	if l2 == nil {
		return l1
	}

	n1, n2 := l1, l2
	for n1 != nil && n2 != nil {
		// l1 is shorter than l2
		if n1.Next == nil && n2.Next != nil {
			l1, l2 = l2, l1
			break
		}

		n1 = n1.Next
		n2 = n2.Next
	}

	addNums(l1, l2, 0)

	return l1
}

func addNums(l1, l2 *ListNode, carryover int) {
	if l2 != nil {
		l1.Val += l2.Val
	} else {

	}

	l1.Val += carryover

	if l1.Val > 9 {
		l1.Val -= 10
		carryover = 1
	} else {
		carryover = 0
	}

	if l1.Next != nil {
		if l2 != nil {
			addNums(l1.Next, l2.Next, carryover)
		} else {
			addNums(l1.Next, nil, carryover)
		}
	} else if carryover > 0 {
		l1.Next = &ListNode{
			Val:  1,
			Next: nil,
		}
	}
}

func addTwoNumbers1(l1 *ListNode, l2 *ListNode) *ListNode {
	s1, s2 := make([]*ListNode, 0, 100), make([]*ListNode, 0, 100)

	node := l1
	for node != nil {
		s1 = append(s1, node)
		node = node.Next
	}

	node = l2
	for node != nil {
		s2 = append(s2, node)
		node = node.Next
	}

	if len(s1) > len(s2) {
		s1, s2 = s2, s1
	}

	var carryover, val, last1, last2 int
	head := s2[0]

	for len(s2) > 0 {
		last1 = len(s1) - 1
		last2 = len(s2) - 1

		if last1 >= 0 {
			val = s1[last1].Val
		} else {
			val = 0
		}

		s2[last2].Val += val + carryover

		if s2[last2].Val > 9 {
			s2[last2].Val -= 10
			carryover = 1
		} else {
			carryover = 0
		}

		if last1 >= 0 {
			s1 = s1[:last1]
		}

		if last2 >= 0 {
			s2 = s2[:last2]
		}
	}

	if carryover > 0 {
		head = &ListNode{
			Val:  1,
			Next: head,
		}
	}

	return head
}
