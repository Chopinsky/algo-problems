'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
    
from hashlib import sha256


class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
    def hash_node(val):
      base = sha256()
      base.update(val.encode('utf-8'))
      return base.hexdigest()

    def merkle_val(node: TreeNode) -> str:
      if not node:
        return '#'
      
      left = merkle_val(node.left)
      right = merkle_val(node.right)
      node.merkle = hash_node(left + str(node.val) + right)
      
      return node.merkle
    
    merkle_val(root)
    merkle_val(subRoot)
    
    def dfs(node: TreeNode) -> bool:
      if not node:
        return False
    
      if node.merkle == subRoot.merkle:
        return True
      
      return dfs(node.left) or dfs(node.right)
    
    return dfs(root)
    
  
  def isSubtree0(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def is_match(s: TreeNode, t: TreeNode):
      if not s and not t:
        return True
      
      if (not s and t) or (s and not t):
        return False
      
      if s.val == t.val:
        return is_match(s.left, t.left) and is_match(s.right, t.right)
      
      return False
    
    if is_match(root, subRoot):
      return True
    
    if not root:
      return False
    
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
  
