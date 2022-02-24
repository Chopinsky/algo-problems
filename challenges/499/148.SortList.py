'''
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 10^4].
-10^5 <= Node.val <= 10^5
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''


from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def mergeSort(h: Optional[ListNode]) -> Optional[ListNode]:
      if not h or not h.next:
        return h
      
      s, f = h, h.next
      if not f.next:
        if s.val <= f.val:
          f.next = None
          return s
        
        f.next = s
        s.next = None
        return f

      while f and f.next:
        s = s.next
        f = f.next.next
        
      # print(s.val)
      rh = s.next
      s.next = None
      
      left = mergeSort(h)
      right = mergeSort(rh)
      h = None
      c = None
      
      while left or right:
        if not left:
          if not h:
            h = right
            break
            
          c.next = right
          break
          
        if not right:
          if not h:
            h = left
            break
            
          c.next = left
          break
          
        if left.val <= right.val:
          nxt = left
          left = left.next
        else:
          nxt = right
          right = right.next
          
        if not h:
          h = nxt
          c = nxt
        else:
          c.next = nxt
          c = c.next
      
      return h
      
    return mergeSort(head)
  