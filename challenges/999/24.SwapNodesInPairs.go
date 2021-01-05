package challenges

/**
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
*/
func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	next := head.Next
	head.Next = next.Next
	next.Next = head

	swap(head, head.Next)

	return next
}

func swap(p, curr *ListNode) {
	if curr == nil || curr.Next == nil {
		return
	}

	next := curr.Next
	curr.Next = next.Next
	next.Next = curr

	p.Next = next
	swap(curr, curr.Next)
}
