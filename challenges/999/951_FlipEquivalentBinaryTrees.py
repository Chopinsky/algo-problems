'''
951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false

Constraints:

The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def flip(node1, node2) -> bool:
      if not node1 and not node2:
        return True
      
      if not node1 or not node2:
        return False
      
      if node1.val != node2.val:
        return False
      
      if flip(node1.left, node2.left) and flip(node1.right, node2.right):
        return True
      
      return flip(node1.right, node2.left) and flip(node1.left, node2.right)
    
    return flip(root1, root2)
  
  def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def check(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
      if not a and not b:
        return True
      
      if (a and not b) or (b and not a):
        return False
      
      if a.val != b.val:
        return False
      
      if check(a.left, b.left) and check(a.right, b.right):
        return True
      
      if check(a.left, b.right) and check(a.right, b.left):
        return True
      
      return False
    
    return check(root1, root2)
    