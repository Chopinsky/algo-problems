package challenges

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	var curr, tail, headSrc *ListNode
	var count int

	curr = head
	for curr != nil {
		tail = curr
		curr = curr.Next
		count++
	}

	if k > count {
		k %= count
	}

	if k == count || k == 0 {
		return head
	}

	count -= k
	curr = head
	headSrc = head

	for count > 0 {
		curr = head
		head = head.Next
		count--
	}

	curr.Next = nil
	tail.Next = headSrc

	return head
}
