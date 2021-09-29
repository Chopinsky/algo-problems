# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def getIntersectionNode(self, a: ListNode, b: ListNode) -> ListNode:
    if not a or not b:
      return None
    
    def get_len(curr: ListNode) -> int:
      count = 0
      
      while curr:
        count += 1
        curr = curr.next
        
      return count
    
    la, lb = get_len(a), get_len(b)
    
    while la > lb:
      a = a.next
      la -= 1
        
    while lb > la:
      b = b.next
      lb -= 1
      
    while a and b:
      if a == b:
        return a
      
      a = a.next
      b = b.next
    
    return None
  