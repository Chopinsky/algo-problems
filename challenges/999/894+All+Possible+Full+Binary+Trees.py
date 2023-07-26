'''
894. All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]

Constraints:

1 <= n <= 20
'''

from typing import List, Optional
from functools import lru_cache


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    @lru_cache(None)
    def dp(n: int):
      if n <= 3:
        if n == 3:
          return [TreeNode(left=TreeNode(), right=TreeNode())]
        
        if n == 1:
          return [TreeNode()]
        
        return []
        
      result = []
      left = 1
      right = n-1-left
      
      while right > 0:
        for lt in dp(left):
          for rt in dp(right):
            result.append(TreeNode(left=lt, right=rt))
        
        left += 1
        right -= 1
      
      return result
    
    return dp(n)
    