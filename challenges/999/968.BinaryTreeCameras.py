# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

'''
Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:

Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:

Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
'''

from typing import List

NOMO_NOCAM = 0
MO_NOCAM = 1
MO_CAM = 2

class Solution:
  def minCameraCover(self, root: TreeNode) -> int:
    count = [0]
    def iterate(node: TreeNode):
      if not node:
        return MO_NOCAM

      left = iterate(node.left)
      right = iterate(node.right)

      # if both left subtree and right subtree are monitored, but left node
      # and right node don't have the camera, the current node is not covered
      # and not monitored
      if left == MO_NOCAM and right == MO_NOCAM:
        return NOMO_NOCAM

      # if either left subnode or right subnode is not covered / has no camera,
      # the current node must have a camera, or the requirements are violated
      if left == NOMO_NOCAM or right == NOMO_NOCAM:
        count[0] += 1
        return MO_CAM

      # if either left node or right node has a camera, the current node is covered,
      # we don't need to place a camera on it
      if left == MO_CAM or right == MO_CAM:
        return MO_NOCAM

      # all other cases, there's no coverage and no camera placed
      return NOMO_NOCAM

    state = iterate(root)
    if state == NOMO_NOCAM:
      return 1 + count[0]

    return count[0]


  def minCameraCover1(self, root: TreeNode) -> int:
    def iterate(root: TreeNode) -> List[int]:
      if not root:
        return [-1, -1, 0]

      if not root.left and not root.right:
        return [1, -1, 0]

      if not root.left or not root.right:
        subtree = iterate(root.left) if root.left else iterate(root.right)
        m = min_count(subtree)

        # print("middle:", subtree)

        n0 = 1 + min_count(subtree)
        n1 = subtree[0] if subtree[0] > 0 else -1
        n2 = subtree[1] if subtree[1] > 0 else -1

        return [n0, n1, n2]

      s1 = iterate(root.left)
      s2 = iterate(root.right)
      m1 = min_count(s1)
      m2 = min_count(s2)

      n0 = 1 + min_count(s1) + min_count(s2)
      n1 = -1
      n2 = -1

      if s1[0] > 0 and (s2[0] > 0 or s2[1] > 0):
        n1 = s1[0] + (min(s2[0], s2[1]) if s2[0] > 0 and s2[1] > 0 else (s2[0] if s2[0] > 0 else s2[1]))

      if s2[0] > 0 and (s1[0] > 0 or s1[1] > 0):
        nt = s2[0] + (min(s1[0], s1[1]) if s1[0] > 0 and s1[1] > 0 else (s1[0] if s1[0] > 0 else s1[1]))
        if n1 < 0 or nt < n1:
          n1 = nt

      if s1[1] > 0 and s2[1] > 0:
        n2 = s1[1] + s2[1]

      # print("middle:", s1, s2, m1, m2)

      return [n0, n1, n2]

    def min_count(arr: List[int]) -> int:
      c = arr[0]
      for i in range(1, len(arr)):
        if c < 0 or (arr[i] >= 0 and arr[i] < c):
          c = arr[i]

      return c

    subtree = iterate(root)
    # print("top:", subtree)

    return min_count(subtree[:2])
