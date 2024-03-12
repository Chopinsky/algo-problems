'''
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
      return None if not head or head.val == 0 else head
    
    fake = ListNode(val=0, next=head)
    curr = head
    stack = [fake]
    prefix = [0]
    seen = set(prefix)
    
    while curr:
      if curr.val == 0:
        curr = curr.next
        continue
        
      curr_prefix = prefix[-1] + curr.val
      if curr_prefix in seen:
        while len(prefix) > 1 and prefix[-1] != curr_prefix:
          p0 = prefix.pop()
          stack.pop()
          seen.discard(p0)
            
      else:
        stack.append(curr)
        prefix.append(curr_prefix)
        seen.add(curr_prefix)
        
      curr = curr.next

    # print([node.val for node in stack])
    if len(stack) == 1:
      return None
    
    for i in range(len(stack)):
      if i < len(stack)-1:
        stack[i].next = stack[i+1]
      else:
        stack[i].next = None
        
    return stack[0].next
        
  def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return head
    
    def reduce(head):
      if not head:
        return head, False
        
      arr = []
      prev = {}
      prefix = 0
      curr = head
      l, r = -1, -1
      
      while curr:
        prefix += curr.val
        idx = len(arr)
        
        if prefix == 0:
          l = -1
          r = idx
        
        if prefix in prev and idx-prev[prefix] > r-l:
          l = prev[prefix]
          r = idx
          
        if prefix not in prev:
          prev[prefix] = idx
          
        arr.append(curr)
        curr = curr.next
        
      found = False
      if r >= 0 and l < 0:
        return arr[r].next, True
      
      if r >= l >= 0:
        arr[l].next = arr[r].next
        arr[r].next = None
        found = True
      
      # print(arr[0].val, found)
      return arr[0], found
    
    curr_head = head
    curr_head, found = reduce(curr_head)
    
    while curr_head and found:
      curr_head, found = reduce(curr_head)
        
    return curr_head  
    