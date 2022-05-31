'''
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


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    def generate(n):
      if n % 2 == 0:
        return []
      
      if n == 1:
        return [TreeNode()]
      
      res = []
      for m in range(1, n):
        l, r = m, n-1-m
        if r < 1:
          break
        
        for lt in generate(l):
          for rt in generate(r):
            root = TreeNode(left=lt, right=rt)
            res.append(root)
            
      return res
        
    return generate(n)
  
  