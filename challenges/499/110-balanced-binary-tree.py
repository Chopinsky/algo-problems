'''
110 Balanced Binary Tree
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def is_balanced(node):
      if not node:
        return True, 0

      lb, ld = is_balanced(node.left)
      rb, rd = is_balanced(node.right)
      # print('iter:', node.val, ld, rd)

      if not lb or not rb:
        return False, -1

      if abs(ld-rd) > 1:
        return False, -1

      return True, 1+max(ld, rd)

    res, _ = is_balanced(root)

    return res
        