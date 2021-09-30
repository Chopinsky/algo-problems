'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    if not root:
      return -1
    
    cache = {}
    def count(root: TreeNode) -> int:
      if not root:
        return 0

      if root in cache:
        return cache[root]

      total = 1 + count(root.left) + count(root.right)
      cache[root] = total

      return total
    
    while k > 0:
      l = count(root.left)
      if l == k-1:
        return root.val

      if l >= k:
        root = root.left
      else:
        root = root.right
        k -= l+1

    return -1
      