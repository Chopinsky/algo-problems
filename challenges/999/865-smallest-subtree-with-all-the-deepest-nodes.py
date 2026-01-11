'''
865-smallest-subtree-with-all-the-deepest-nodes
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    cnt = []

    def dfs(node, l):
      if not node:
        return

      if l >= len(cnt):
        cnt.append(1)
      else:
        cnt[l] += 1

      dfs(node.left, l+1)
      dfs(node.right, l+1)

    dfs(root, 0)
    # print('init:', cnt)

    def search(node, l):
      if not node:
        return 0, None

      if l == len(cnt)-1:
        return 1, node

      lc, lr = search(node.left, l+1)
      rc, rr = search(node.right, l+1)
      
      if lc == cnt[-1]:
        return lc, lr

      if rc == cnt[-1]:
        return rc, rr

      if lc+rc == cnt[-1]:
        return lc+rc, node

      return lc+rc, None

    _, subtree = search(root, 0)

    return subtree
        