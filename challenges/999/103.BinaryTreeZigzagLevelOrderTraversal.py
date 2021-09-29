'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''


from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []
    
    ans = []
    stack = [root]
    nxt = []
    reverse = False
    
    while stack:
      r = []
      
      for node in stack:
        r.append(node.val)
        if node.left:
          nxt.append(node.left)
        
        if node.right:
          nxt.append(node.right)
          
      if reverse:
        r.reverse()
        
      ans.append(r)
      reverse = not reverse
      
      stack, nxt = nxt, stack
      nxt.clear()
      
    return ans
  