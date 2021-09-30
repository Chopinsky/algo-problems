'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    back, front = head, head

    # move front with n-offsets
    for i in range(n):
      front = front.next

    # n == len(list), pop the head and done
    if front is None:
      return head.next

    # move back and front together, when front reaches the end of the
    # list, then back is right at (n-1)th node from the end of the list.
    while front and front.next:
      front = front.next
      back = back.next

    # now remove the nth node (next node to the back node) from the list
    back.next = back.next.next

    return head


  def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
    if head is None or n == 0:
      return head

    if head.next is None and n > 0:
      return None

    stack = [None] * 31
    idx = 0
    curr = head

    while curr is not None:
      stack[idx] = curr
      curr = curr.next
      idx += 1

    idx -= n
    if idx == 0:
      stack[0].next = None
      return stack[1]

    stack[idx].next = None
    stack[idx-1].next = stack[idx+1]

    # print(stack)
    return head