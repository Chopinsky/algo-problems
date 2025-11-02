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
    if not head:
      return head

    fake_head = ListNode(val=0, next=head)
    val_set = set(nums)
    curr = fake_head

    while curr and curr.next:
      # print('curr:', curr.val, curr.next.val)
      if curr.next.val in val_set:
        old = curr.next
        curr.next = old.next
        old.next = None
      else:
        curr = curr.next

    return fake_head.next
        