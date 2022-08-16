'''
958. Check Completeness of a Binary Tree

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:


Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:


Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    if not root:
      return False
    
    curr, nxt = [root], []
    count = 1
    
    while curr:
      for node in curr:
        nxt.append(node.left)
        nxt.append(node.right)
        
      while nxt and nxt[-1] is None:
        nxt.pop()
        
      for node in nxt:
        if node is None:
          return False
      
      if nxt and len(curr) < count:
        # print(len(curr), count, nxt)
        return False
      
      curr, nxt = nxt, curr
      count <<= 1
      nxt.clear()
      
    return True
  