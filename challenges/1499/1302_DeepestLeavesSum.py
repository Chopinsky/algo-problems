'''
Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
1 <= Node.val <= 100
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    lvl_sum = []
    
    def add(root: Optional[TreeNode], lvl: int):
      if not root:
        return
      
      if len(lvl_sum) <= lvl:
        lvl_sum.append(root.val)
      else:
        lvl_sum[lvl] += root.val
        
      add(root.left, lvl+1)
      add(root.right, lvl+1)
      
    add(root, 0)
      
    return lvl_sum[-1]
    