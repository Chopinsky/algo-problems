'''
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

Example 1:

Input: root = [5,4,5,1,1,5]
Output: 2

Example 2:

Input: root = [1,4,5,4,4,5]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000
The depth of the tree will not exceed 1000.
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    ans = 0
    
    def iterate(root: Optional[TreeNode], p: int) -> int:
      nonlocal ans
      
      if not root:
        return 0
        
      lc = iterate(root.left, root.val)
      rc = iterate(root.right, root.val)
      # print(root.val, lc, rc)
      ans = max(ans, lc+rc)
      
      if root.val == p:
        return 1 + max(lc, rc)
      
      return 0
    
    lc = iterate(root.left, root.val)
    rc = iterate(root.right, root.val)
    ans = max(ans, lc+rc)
    # print('root', lc, rc)
    
    return ans
  