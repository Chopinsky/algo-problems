'''
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1:
      return l2
    
    if not l2:
      return l1
    
    carryover = 0
    s1, s2 = [], []
    curr = l1
    
    while curr:
      s1.append(curr)
      curr = curr.next
      
    curr = l2
    while curr:
      s2.append(curr)
      curr = curr.next
      
    if len(s1) < len(s2):
      s1, s2 = s2, s1
      
    head = None
    while s1:
      n1 = s1.pop()
      n2 = s2.pop() if s2 else None
      
      n1.val += carryover + (n2.val if n2 else 0)
      if n1.val > 9:
        carryover = 1
        n1.val -= 10
      else:
        carryover = 0
      
      head = n1
      
    if carryover == 1:
      head = ListNode(val=1, next=head)
      
    return head
        