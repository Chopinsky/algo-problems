# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def goodNodes(self, root: TreeNode) -> int:
    def iterate(root: TreeNode, top: int) -> int:
      if not root:
        return 0
      
      top = max(root.val, top)
      return iterate(root.left, top) + iterate(root.right, top) + (1 if root.val >= top else 0)
    
    return iterate(root, root.val if root else 0)