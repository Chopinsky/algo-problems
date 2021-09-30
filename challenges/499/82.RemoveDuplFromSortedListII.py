'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''


from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return head
    
    fake = ListNode(-101, head)
    curr = fake
    
    def shift(curr: ListNode) -> Optional[ListNode]:
      if not curr or not curr.next or curr.val != curr.next.val:
        return curr
      
      base = curr.val
      curr = curr.next
      
      while curr and curr.val == base:
        curr = curr.next
        
      return curr
    
    while curr:
      nxt_val = curr.next
      nxt_node = shift(curr.next)
      
      while nxt_node and nxt_val != nxt_node.val:
        nxt_val = nxt_node.val
        nxt_node = shift(nxt_node)
      
      curr.next = nxt_node
      curr = curr.next
      # print(curr.val)
      
    return fake.next