'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 
Constraints:

The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000
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
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    max_sum = root.val
    
    def dp(root):
      nonlocal max_sum
      if not root:
        return -math.inf
      
      lm, rm = dp(root.left), dp(root.right)
      max_sum = max(max_sum, lm, rm, root.val, root.val+lm, root.val+rm, root.val+lm+rm)
      
      return max(root.val, root.val+lm, root.val+rm)    
      
    dp(root)
      
    return max_sum


  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    max_val = -math.inf
    
    def iterate(root):
      nonlocal max_val
      if not root:
        return 0
      
      vl, vr = iterate(root.left), iterate(root.right)
      max_val = max(max_val, root.val, root.val+vl, root.val+vr, root.val+vl+vr)
      
      return max(root.val, root.val+vl, root.val+vr)
      
    iterate(root)
    
    return max_val
  