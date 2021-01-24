package challenges

/**
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
*/
func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	}

	h := make(queue, 0, 128)
	var curr, head *ListNode

	for i, node := range lists {
		if node != nil {
			h.Push([]int{node.Val, i})
		}
	}

	for h.Len() > 0 {
		top := h.Pop().([]int)
		idx := top[1]

		if curr != nil {
			curr.Next = lists[idx]
			curr = curr.Next
		} else {
			curr = lists[idx]
			head = curr
		}

		lists[idx] = curr.Next
		if lists[idx] != nil {
			h.Push([]int{lists[idx].Val, idx})
		}
	}

	// fmt.Println(h)

	return head
}
