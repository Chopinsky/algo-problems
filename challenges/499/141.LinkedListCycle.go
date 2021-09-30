package challenges

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
	f, s := head, head

	for s != nil && f != nil {
		s = s.Next
		f = f.Next

		if f != nil {
			f = f.Next
			if f == s {
				return true
			}
		}
	}

	return false
}
