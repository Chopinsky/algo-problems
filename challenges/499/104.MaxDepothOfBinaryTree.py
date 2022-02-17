'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    stack, nxt = [root], []
    depth = 0
    
    while stack:
      for node in stack:
        if node.left:
          nxt.append(node.left)
          
        if node.right:
          nxt.append(node.right)
      
      depth += 1
      stack, nxt = nxt, stack
      nxt.clear()
    
    return depth
  