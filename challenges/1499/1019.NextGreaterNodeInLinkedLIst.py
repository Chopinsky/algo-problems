'''
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

Example 1:


Input: head = [2,1,5]
Output: [5,5,0]
Example 2:


Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 104
1 <= Node.val <= 109
'''


from typing import Optional, List
from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    idx = 0
    res = defaultdict(int)
    stack = []
    
    while head:
      while stack and stack[-1][0] < head.val:
        _, jdx = stack.pop()
        res[jdx] = head.val
      
      stack.append((head.val, idx))
      head = head.next
      idx += 1
      
    # print(res)
    return [res[i] for i in range(idx)]
    