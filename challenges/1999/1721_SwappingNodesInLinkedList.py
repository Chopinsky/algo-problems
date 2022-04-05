'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 10^5
0 <= Node.val <= 100
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
      return head
    
    arr = []
    curr = head
    while curr:
      arr.append(curr)
      curr = curr.next
      
    n = len(arr)
    i, j = k-1, n-k
    if i == j:
      return arr[0]
    
    arr[i], arr[j] = arr[j], arr[i]
    if i > 0:
      arr[i-1].next = arr[i]
    
    if j > 0:
      arr[j-1].next = arr[j]
      
    arr[i].next = arr[i+1] if i < n-1 else None
    arr[j].next = arr[j+1] if j < n-1 else None
    
    return arr[0]
        