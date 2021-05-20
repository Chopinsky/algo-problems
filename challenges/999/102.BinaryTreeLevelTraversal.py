# Definition for a binary tree node.

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

from typing import List

class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
      return []

    ans = []
    level = [root]
    next_lvl = []

    while len(level) > 0:
      curr = []

      for n in level:
        curr.append(n.val)
        if n.left:
          next_lvl.append(n.left)

        if n.right:
          next_lvl.append(n.right)

      level, next_lvl = next_lvl, level
      next_lvl.clear()

      ans.append(curr)

    return ans
