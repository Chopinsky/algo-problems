package challenges

/**
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Example 3:

Input: head = [1], k = 1
Output: [1]

Example 4:

Input: head = [1,2], k = 1
Output: [2,1]

Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100

 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
*/
func swapNodes(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}

	var kfp, kf, kbp, kb *ListNode
	count := 1
	node := head

	for node != nil {
		if count == k-1 {
			kfp = node
		} else if count == k {
			kf = node
		}

		node = node.Next
		count++
	}

	node = head
	size := count - 1

	for node != nil {
		count--
		if count == k+1 {
			kbp = node
		} else if count == k {
			kb = node
		}

		node = node.Next
	}

	// fmt.Println(kfp, kf, kbp, kb)

	// no need to swap
	if kf == kb {
		return head
	}

	// switch
	if k > size/2 {
		kfp, kbp = kbp, kfp
		kf, kb = kb, kf
	}

	if kf == kbp {
		if kfp != nil {
			kfp.Next = kb
		}

		temp := kb.Next
		kb.Next = kf
		kf.Next = temp

		if kfp != nil {
			return head
		}

		return kb
	}

	if kfp != nil {
		kfp.Next = kb
	}

	temp := kb.Next
	kb.Next = kf.Next

	kbp.Next = kf
	kf.Next = temp

	if kfp != nil {
		return head
	}

	return kb
}
