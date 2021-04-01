package challenges

/**
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?

 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
*/

func isPalindrome(head *ListNode) bool {
	var rev *ListNode
	f, s := head, head

	for (f != nil) && (f.Next != nil) {
		// move fast
		f = f.Next.Next

		// save off temp rev head
		temp := rev
		rev = s

		// move slow
		s = s.Next
		rev.Next = temp
	}

	// if odd numbers
	if f != nil {
		s = s.Next
	}

	// check palindrome
	for rev != nil && rev.Val == s.Val {
		rev, s = rev.Next, s.Next
	}

	// end of the list == true, otherwise, false
	return rev == nil
}

func isPalindrome1(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}

	var ln int

	curr := head
	for curr != nil {
		ln++
		curr = curr.Next
	}

	odd := ln%2 == 1
	ln /= 2
	curr = head
	stack := make([]int, 0, ln)

	for curr != nil {
		val := curr.Val
		curr = curr.Next

		if ln > 0 {
			stack = append(stack, val)
			ln--
			continue
		}

		ln--
		if ln == -1 && odd {
			continue
		}

		// fmt.Println(stack, ln, val)

		last := len(stack) - 1
		if stack[last] != val {
			return false
		}

		stack = stack[:last]
	}

	return true
}
