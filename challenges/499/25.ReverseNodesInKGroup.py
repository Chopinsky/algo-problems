'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:

Input: head = [1], k = 1
Output: [1]
 

Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz

Follow-up: Can you solve the problem in O(1) extra memory space?
'''


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    if k == 1:
      return head
    
    def reverse(h: ListNode, k: int):
      curr = h
      count = 0
      
      while curr:
        count += 1
        if count == k:
          break
          
        curr = curr.next
        
      if count < k:
        return h, None, None, True
      
      tail = h
      curr = h
      last = None
      count = 0
      
      while count < k:
        count += 1
        temp = curr.next
        curr.next = last
        last = curr
        curr = temp

      return last, tail, curr, False
    
    rh, last = None, None
    h = head
    done = False
    
    while not done:
      h0, t, h1, done = reverse(h, k)
      # print(h.val if h else None, t.val if t else None, done)
      
      if not rh:
        rh = h0
        
      if last:
        last.next = h0
        
      last = t
      h = h1
    
    return rh
  