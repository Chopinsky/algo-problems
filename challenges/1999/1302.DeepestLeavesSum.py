'''
Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def deepestLeavesSum(self, root: TreeNode) -> int:
    ans = self.sum(root, 0)
    return ans[1]

  def sum(self, root: TreeNode, level: int) -> (int, int):
    if not root:
      return (-1, 0)

    lval = self.sum(root.left, level+1)
    rval = self.sum(root.right, level+1)

    if lval[0] < 0 and rval[0] < 0:
      return (level, root.val)

    if lval[0] < 0:
      return rval

    if rval[0] < 0:
      return lval

    if lval[0] == rval[0]:
      return (lval[0], lval[1]+rval[1])

    return rval if lval[0] < rval[0] else lval

