package challenges

// ListNode ...
type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getDecimalValue(head *ListNode) int {
	num := 0

	for head != nil {
		num <<= 1
		num |= head.Val
		head = head.Next
	}

	return num
}
