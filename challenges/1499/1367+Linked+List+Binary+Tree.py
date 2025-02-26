'''
1367. Linked List in Binary Tree
'''

from typing import Optional
from functools import lru_cache

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
        
class Solution:
  def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    vals = []
    curr = head
    
    while curr:
      vals.append(curr.val)
      curr = curr.next
      
    n = len(vals)
    # print('init:', vals)
    
    @lru_cache(None)
    def dp(node, idx: int) -> bool:
      if idx >= n:
        # print('0-true:', idx)
        return True
      
      if not node:
        # print('0-false:', idx)
        return False
      
      # continue the chain
      if node.val == vals[idx] and (dp(node.left, idx+1) or dp(node.right, idx+1)):
        # print('1:', node.val, idx)
        return True
        
      # start as the head
      idx = 0
      if node.val == vals[idx] and (dp(node.left, idx+1) or dp(node.right, idx+1)):
        # print('2:', node.val, idx)
        return True

      # start from the child
      return dp(node.left, idx) or dp(node.right, idx)
      
    return dp(root, 0)
        