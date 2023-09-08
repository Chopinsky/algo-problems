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

from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if left == right:
      return head
    
    def reverse(head, count):
      if not head:
        return head
      
      curr, tail = head, head
      prev = None
      
      while curr and count > 0:
        # print('iter:', curr.val, count)
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        count -= 1
        
      tail.next = curr
      # print('end:', prev.val, tail.val, curr.val if curr else None)
      
      return prev
    
    if left == 1:
      return reverse(head, right-left+1)
    
    curr = head
    idx = 1
    
    while idx+1 < left:
      curr = curr.next
      idx += 1
    
    # print('curr:', curr.val)
    curr.next = reverse(curr.next, right-left+1)
    
    return head
  

  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    fake_head = ListNode(val=-1, next=head)
    idx = 0
    last = None 
    curr = fake_head
    
    while idx < left:
      last = curr
      curr = curr.next
      idx += 1
      
    # print(last.val, curr.val)
    stack = [curr]
    tail = curr.next
    
    while idx < right and curr:
      curr = curr.next
      stack.append(curr)
      tail = curr.next
      idx += 1
      
    # print(curr.val, tail)
    for i in range(len(stack)):
      if i == 0:
        stack[i].next = tail
      else:
        stack[i].next = stack[i-1]
        
    last.next = stack[-1]
    return fake_head.next


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
    