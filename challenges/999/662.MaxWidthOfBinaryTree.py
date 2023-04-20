'''
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,null,5,3]
Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
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
  def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    max_id, min_id = {}, {}
    
    def dp(root, level, idx):
      if not root:
        return 
      
      max_id[level] = max(max_id.get(level, 0), idx)
      min_id[level] = min(min_id.get(level, math.inf), idx)
      
      dp(root.left, level+1, 2*idx)
      dp(root.right, level+1, 2*idx+1)
      
    dp(root, 0, 0)
    max_width = 0
    # print(max_id, min_id)
    
    for lvl in max_id:
      max_width = max(max_width, max_id[lvl] - min_id[lvl])
      
    return max_width+1
  

  def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    stack, nxt = [(0, root)], []
    width = 0
    
    while stack:
      width = max(width, stack[-1][0]-stack[0][0]+1)
      
      for idx, node in stack:
        if node.left:
          nxt.append((idx<<1, node.left))
          
        if node.right:
          nxt.append(((idx<<1)+1, node.right))
      
      stack, nxt = nxt, stack
      nxt.clear()
      
    return width  
      