'''
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 
Constraints:

The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1
 

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def recoverTree(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    nodes = []
    last = None
    
    # use in-order traverse to detech abonomalties in the
    # increamental sequence -- swap the 2 nodes whose number
    # appears out of the place.
    def inorder(root):
      nonlocal last
      if not root:
        return
      
      inorder(root.left)
      
      # normal order, update and continue
      if not last or root.val > last.val:
        last = root
        
      # abnomalty detected, store notes of 
      # these nodes to restore the orders
      else:
        if not nodes:
          nodes.append(last)
          nodes.append(root)
          last = root
        else:
          nodes[1] = root
          
      inorder(root.right)
      
    inorder(root)
    nodes[0].val, nodes[1].val = nodes[1].val, nodes[0].val
    