'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
    
class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ans = []
    stack = [(root, 2)]
    
    while stack:
      node, state = stack.pop()
      if not node:
        continue
        
      if state == 2:
        stack.append((node, 1))
        stack.append((node.left, 2))
        continue
        
      if state == 1:
        ans.append(node.val)
        stack.append((node.right, 2))
    
    return ans
  
