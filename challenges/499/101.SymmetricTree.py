'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
'''


from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
      return True
    
    stack = [(root.left, root.right)]
    
    while stack:
      l, r = stack.pop()
      if not l and not r:
        continue
        
      if not l or not r or (l.val != r.val):
        return False
      
      stack.append((l.right, r.left))
      stack.append((l.left, r.right))
    
    return True
    