'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
      iidx = {}

      '''
      get root node's idx, this is also the index to divide the left tree
      and right tree in `preorder`
      '''
      for idx, val in enumerate(inorder):
        iidx[val] = idx

      pidx = 0

      '''
      idea is to build the left-tree first, and in this scheme, preorder-index
      will be mono-increasing, since preorder[pidx] is always the root of the
      left tree; we just need to mark the left/right tree boundaries for leaf
      nodes.
      '''
      def array_to_tree(left: int, right: int) -> TreeNode:
        nonlocal pidx

        # leaf node
        if left > right:
          return None

        val = preorder[pidx]
        root = TreeNode(val)
        pidx += 1

        # divide the `preorder` array into the `left` and `right` tree segements,
        # and rebuild the tree in each segments
        root.left = array_to_tree(left, iidx[val] - 1)
        root.right = array_to_tree(iidx[val] + 1, right)

        return root

      return array_to_tree(0, len(preorder) - 1)


  def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    n = len(preorder)

    if n == 0:
      return None

    val = preorder[0]
    root = TreeNode(val)

    if n == 1:
      return root

    left = set()
    ii = 0
    pi = 1

    while ii < n:
      if inorder[ii] == val:
        break

      left.add(inorder[ii])
      ii += 1

    while pi < n:
      if preorder[pi] not in left:
        break

      pi += 1

    # print(val, pi, ii, "left:", preorder[1:pi], inorder[:ii], "; right:", preorder[pi:], inorder[ii+1:])

    if ii > 0:
      root.left = self.buildTree(preorder[1:pi], inorder[:ii])

    if ii+1 < n:
      root.right = self.buildTree(preorder[pi:], inorder[ii+1:])

    return root
