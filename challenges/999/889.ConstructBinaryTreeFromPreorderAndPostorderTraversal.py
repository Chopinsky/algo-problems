'''
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
 

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
'''


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right



class Solution:
  def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def build(pre: List[int], post: List[int]) -> Optional[TreeNode]:
      if not pre:
        return None
      
      root = TreeNode(val=pre[0])
      if len(pre) == 1:
        return root
      
      rval = post[-2]
      idx = 2
      
      while idx < len(pre) and pre[idx] != rval:
        idx += 1
        
      root.left = build(pre[1:idx], post[:idx-1])
      root.right = build(pre[idx:], post[idx-1:-1])
      return root
    
    return build(preorder, postorder)
        