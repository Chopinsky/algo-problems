'''
783. Minimum Distance Between BST Nodes

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1
Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 10^5

Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
'''

from typing import Optional
import math


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    last = -1
    ans = math.inf
        
    def inorder(node):
      nonlocal last, ans
      if not node:
        return
      
      inorder(node.left)
      if last >= 0:
        ans = min(ans, node.val - last)
      
      last = node.val
      inorder(node.right)
    
    inorder(root)
    
    return ans
    