'''
Given the root of a binary tree, return the sum of all left leaves.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:

Input: root = [1]
Output: 0

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    def sum_left_leaves(root, is_left):
      if not root:
        return 0
      
      if not root.left and not root.right and is_left:
        return root.val
      
      return sum_left_leaves(root.left, True) + sum_left_leaves(root.right, False)
      
    return sum_left_leaves(root, False)
    
  def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    total = 0
    
    def iterate(root: Optional[TreeNode], is_left: bool):
      nonlocal total
      
      if not root:
        return
      
      if not root.left and not root.right and is_left:
        total += root.val
        return
      
      iterate(root.left, True)
      iterate(root.right, False)
      
    iterate(root, False)
    
    return total