package challenges

/**
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100

The list is guaranteed to be sorted in ascending order.

 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
*/
func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	var tail *ListNode
	curr := head
	next := curr.Next
	head = nil

	for curr != nil {
		if next != nil && curr.Val == next.Val {
			for next != nil && curr.Val == next.Val {
				next = next.Next
			}

			if next == nil {
				break
			}

			curr = next
			next = curr.Next

			continue
		}

		if head == nil {
			head = curr
			tail = curr
		} else {
			tail.Next = curr
			tail = tail.Next
		}

		curr = curr.Next

		if curr != nil {
			next = curr.Next
		} else {
			next = nil
		}

		tail.Next = nil
	}

	return head
}
