'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1
'''


import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def check(root, low, high):
      if not root:
        return True
      
      if root.val <= low or root.val >= high:
        return False
      
      if root.left and root.val <= root.left.val:
        return False
      
      if root.right and root.val >= root.right.val:
        return False
      
      return check(root.left, low, root.val) and check(root.right, root.val, high)
    
    return check(root, -math.inf, math.inf)
    

  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def validate(root: Optional[TreeNode], low: int, high: int) -> bool:
      if not root:
        return True
      
      if root.val >= high or root.val <= low:
        return False
      
      return validate(root.left, low, root.val) and validate(root.right, root.val, high)
      
      
    return validate(root, -math.inf, math.inf)
  