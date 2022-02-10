'''
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:

Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:    
    stack, nxt = [root], []
    left = root
    
    while stack:
      left = stack[0]
      for node in stack:
        if node.left:
          nxt.append(node.left)
        
        if node.right:
          nxt.append(node.right)
        
      stack, nxt = nxt, stack
      nxt.clear()
      
    return left.val
  