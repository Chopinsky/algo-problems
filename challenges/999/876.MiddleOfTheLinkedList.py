'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''


from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    s, f = head, head
    last = None
    
    while f:
      # print(s.val, f.val)
      last = s
      s = s.next
      f = f.next
      if not f:
        return last
        
      if f:
        f = f.next
      
    return s
    
  
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return None
    
    s, f = head, head
    
    while f.next:
      s = s.next
      f = f.next
      
      if not f.next:
        break
        
      f = f.next
      
    return s
  