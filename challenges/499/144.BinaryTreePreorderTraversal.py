'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [1,2]

Example 5:

Input: root = [1,null,2]
Output: [1,2]
 

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
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    
    def traverse(root):
      if not root:
        return
      
      res.append(root.val)
      traverse(root.left)
      traverse(root.right)
      
    traverse(root)
    
    return res


  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ans = []
    stack = [(root, 2)]
    
    while stack:
      node, state = stack.pop()
      if not node or not state:
        continue
      
      if state == 2:
        ans.append(node.val)
        stack.append((node, 1))
        stack.append((node.left, 2))
        continue
        
      if state == 1:
        stack.append((node.right, 2))
        
    return ans
  
