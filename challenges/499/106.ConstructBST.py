'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
'''


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    idx_map = {val: idx for idx, val in enumerate(inorder)}

    def traverse(left: int, right: int):
      if left > right:
        return None
      
      val = postorder.pop()
      root = TreeNode(val)
      index = idx_map[val]
      
      root.right = traverse(index+1, right)
      root.left = traverse(left, index-1)
      
      return root

    return traverse(0, len(inorder)-1)
      
    
  def buildTree0(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def construct(io: List[int], po: List[int]) -> Optional[TreeNode]:
      if not io:
        return None

      rval = po[-1]
      root = TreeNode(rval)
      idx = 0
      
      while idx < len(io):
        if io[idx] == rval:
          break
          
        idx += 1
        
      root.left = construct(io[:idx], po[:idx])
      root.right = construct(io[idx+1:], po[idx:-1])
      
      return root
    
    return construct(inorder, postorder)
  