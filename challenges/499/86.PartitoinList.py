'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    small_head = ListNode()
    small = small_head
    large_head = ListNode()
    large = large_head
    curr = head
    
    while curr:
      nxt = curr.next
      if curr.val < x:
        small.next = curr
        small = small.next
        small.next = None
        
      else:
        large.next = curr
        large = large.next
        large.next = None
        
      curr = nxt
    
    if not small_head.next:
      return large_head.next
    
    if not large_head.next:
      return small_head.next
    
    if small:
      small.next = large_head.next
      large_head.next = None
      
    head = small_head.next
    small_head.next = None
    
    return head
    

  def partition(self, head: ListNode, x: int) -> ListNode:
    if head is None:
      return head

    dummy1 = ListNode(-1)
    dummy2 = ListNode(-1)
    e1, e2 = dummy1, dummy2

    while head:
      if head.val < x:
        e1.next = head
        e1 = e1.next
      else:
        e2.next = head
        e2 = e2.next

      head = head.next

    e2.next = None
    e1.next = dummy2.next

    return dummy1.next


  def partition1(self, head: ListNode, x: int) -> ListNode:
    greater, greaterTail = None, None
    lesser, lesserTail = None, None
    curr = head

    while curr is not None:
      nextNode = curr.next

      if curr.val < x:
        if lesser is None:
          lesser = curr
          lesserTail = curr
        else:
          lesserTail.next = curr
          lesserTail = lesserTail.next

      else:
        if greater is None:
          greater = curr
          greaterTail = curr
        else:
          greaterTail.next = curr
          greaterTail = greaterTail.next

      curr.next = None
      curr = nextNode


    if lesser is not None:
      head = lesser
      lesserTail.next = greater
    else:
      head = greater

    return head
