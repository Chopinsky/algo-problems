'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''


from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    if not head or not head.next:
      return
    
    stack = []
    curr = head
    
    while curr:
      stack.append(curr)
      curr = curr.next
    
    i, j = 0, len(stack)-1
    tail = None
    
    while i <= j:
      if tail:
        tail.next = stack[i]
      
      stack[i].next = stack[j]
      stack[j].next = None
      tail = stack[j]
      
      i += 1
      j -= 1
    
    return
      
  def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head:
      return 
    
    stack = []
    curr = head
    
    while curr:
      stack.append(curr)
      curr = curr.next
      
    curr = head
    stack = stack[1:]
    
    while stack:
      curr.next = stack.pop()
      curr = curr.next
      
      if stack:
        curr.next = stack[0]
        curr = curr.next
        stack = stack[1:]
        
    curr.next = None
    