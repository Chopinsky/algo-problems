'''
1669. Merge In Between Linked Lists

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.

Example 1:


Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
Example 2:


Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.
 

Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104
'''

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    head = ListNode(val=-1, next=list1)
    idx = 0
    curr = head
    start = None
    end = None
    
    while curr:
      # print(idx, curr.val)
      if idx == a:
        start = curr
        
      if idx-1 == b:
        end = curr.next
        break
      
      curr = curr.next
      idx += 1
      
    curr = list2
    while curr.next:
      curr = curr.next
    
    start.next = list2
    curr.next = end
    
    return head.next
        
  def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    prev, nxt = None, None
    curr = list1
    idx = 0
    
    while curr:
      if idx == a:
        prev = last
        
      if idx == b:
        break
        
      last = curr
      curr = curr.next
      idx += 1
      
    # print(prev.val, nxt.val)
    nxt = curr.next
    curr.next = None
    
    head = list1 if prev else list2
    if prev:
      prev.next = list2
      
    curr = list2
    while curr.next:
      curr = curr.next
      
    curr.next = nxt
    
    return head
  