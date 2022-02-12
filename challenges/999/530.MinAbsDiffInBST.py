'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:

The number of nodes in the tree is in the range [2, 10^4].
0 <= Node.val <= 10^5

Note: This question is the same as 783: 
https://leetcode.com/problems/minimum-distance-between-bst-nodes/
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
  def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    vals = []
    
    def add_val(node: TreeNode):
      if not node:
        return
      
      add_val(node.left)
      vals.append(node.val)
      add_val(node.right)
      
    add_val(root)
    
    return min(vals[i]-vals[i-1] for i in range(1, len(vals)))
    
    
  def getMinimumDifference0(self, root: Optional[TreeNode]) -> int:
    last = None
    stack = []
    curr = root
    min_val = math.inf
    
    while curr:
      stack.append(curr)
      curr = curr.left
      
    while stack and min_val > 0:
      curr = stack.pop()
      if not curr:
        continue
        
      if last:
        min_val = min(min_val, abs(curr.val - last.val))
        
      last = curr
      
      if curr.right:
        last = curr
        curr = curr.right
        
        while curr:
          stack.append(curr)
          curr = curr.left
        
    return min_val
      