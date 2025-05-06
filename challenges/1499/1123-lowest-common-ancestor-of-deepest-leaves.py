'''
1123-lowest-common-ancestor-of-deepest-leaves
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    levels = -1
    leaves_count = 0
    ans = [0, root]

    def dfs(curr, lvl: int):
      nonlocal levels, leaves_count

      if not curr:
        return

      if lvl > levels:
        levels = lvl
        leaves_count = 0

      if lvl == levels:
        leaves_count += 1

      dfs(curr.left, lvl+1)
      dfs(curr.right, lvl+1)

    def lca(curr, lvl: int) -> int:
      if not curr:
        return 0

      if lvl == levels:
        count = 1
      else:
        count = lca(curr.left, lvl+1) + lca(curr.right, lvl+1)

      if count == leaves_count and lvl > ans[0]:
        ans[0] = lvl
        ans[1] = curr

      return count

    dfs(root, 0)
    # print('init:', levels, leaves_count)
    lca(root, 0)

    return ans[1]
