'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []
    
    stack = []
    level, nxt = [root], []
    
    while level:
      stack.append(level[-1].val)
      for node in level:
        if node.left:
          nxt.append(node.left)
          
        if node.right:
          nxt.append(node.right)
          
      level, nxt = nxt, level
      nxt.clear()
      
    return stack


  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []
    
    tree = {}
    def iterate(root: TreeNode, level: int):
      if not root:
        return 
      
      if level not in tree:
        tree[level] = root.val
        
      iterate(root.right, level+1)
      iterate(root.left, level+1)
      
    iterate(root, 0)
    ans = []
    
    for l in sorted(tree):
      ans.append(tree[l])
      
    return ans