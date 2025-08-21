'''
3319-k-th-largest-perfect-subtree-size-in-binary-tree
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
    size = []

    def is_perfect(root):
      if not root:
        return True, 0

      lt, lc = is_perfect(root.left)
      rt, rc = is_perfect(root.right)
      if lt and rt and lc == rc:
        tree_size = 1+lc+rc
        size.append(tree_size)
        # print('iter:', root.val, tree_size)

        return True, tree_size

      return False, 0

    is_perfect(root)
    size.sort()
    # print('done:', size)

    return -1 if len(size) < k else size[-k]
        