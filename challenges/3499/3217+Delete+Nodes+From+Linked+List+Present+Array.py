'''
3217. Delete Nodes From Linked List Present in Array
'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    fake_head = ListNode(val=0, next=head)
    nums = set(nums)
    curr = fake_head
    
    while curr and curr.next:
      if curr.next.val in nums:
        node = curr.next.next
        curr.next.next = None
        curr.next = node
      else:
        curr = curr.next
    
    return fake_head.next
        