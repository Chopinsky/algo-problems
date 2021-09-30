'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
'''


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    if left == right or not head or not head.next:
      return head
    
    lb, rb, l = None, None, None
    curr = head
    pos = 1
    
    def reverse(h: ListNode, t: ListNode) -> ListNode:
      curr = h
      last = t
      
      while curr:
        temp = curr.next
        curr.next = last
        last = curr
        curr = temp
        
      return last
    
    while curr:
      if pos == left-1:
        lb = curr
      elif pos == left:
        l = curr
      elif pos == right:
        rb = curr.next
        curr.next = None
        
      pos += 1
      curr = curr.next
      
    # print(l.val)
    
    front = reverse(l, rb)
    
    if not lb:
      return front
    
    lb.next = front
    return head
    