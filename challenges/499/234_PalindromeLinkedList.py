'''
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    vals = []
    while head:
      vals.append(head.val)
      head = head.next
      
    i, j = 0, len(vals)-1
    while i < j:
      if vals[i] != vals[j]:
        return False
      
      i += 1
      j -= 1
      
    return True
  
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    if not head:
      return True
    
    stack = []
    while head:
      stack.append(head.val)
      head = head.next
      
    i, j = 0, len(stack)-1
    while i < j:
      if stack[i] != stack[j]:
        return False
      
      i += 1
      j -= 1
    
    return True
  