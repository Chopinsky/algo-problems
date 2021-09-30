package challenges

import "math/rand"

/**
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?
*/

// LLRNSolution ...
type LLRNSolution struct {
	head *ListNode
}

// LLRNConstructor ...
// @param head The linked list's head.
//  Note that the head is guaranteed to be not null, so it contains at least one node.
func LLRNConstructor(head *ListNode) LLRNSolution {
	return LLRNSolution{
		head: head,
	}
}

// GetRandom ... the idea is to check if we can
// change the number from the later of the array
// with arr[0], i.e. reservior sampling with k = 1
func (t *LLRNSolution) GetRandom() int {
	numRange := 1
	val := t.head.Val
	curr := t.head

	for curr != nil {
		if rand.Intn(numRange) < 1 {
			val = curr.Val
		}

		numRange++
		curr = curr.Next
	}

	return val
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(head);
 * param_1 := obj.GetRandom();
 */
