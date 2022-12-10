'''
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025

Example 4:

Input: root = [1,1]
Output: 1

Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
'''

from typing import Optional
from functools import lru_cache


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxProduct(self, root: Optional[TreeNode]) -> int:
    @lru_cache(None)
    def subtree_sum(root):
      if not root:
        return 0
      
      return root.val + subtree_sum(root.left) + subtree_sum(root.right)
    
    total = subtree_sum(root)
    mod = 10**9+7
    # print(total)
    
    def check(root):
      base = 0
      if root.left:
        lt = subtree_sum(root.left)
        # print('left', root.val, lt)
        base = max(base, (total-lt)*lt, check(root.left))
        
      if root.right:
        rt = subtree_sum(root.right)
        # print('right', root.val, rt)
        base = max(base, (total-rt)*rt, check(root.right))
      
      return base
    
    return check(root) % mod
    

  def maxProduct(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    subtrees = set()
    
    def iterate(root: TreeNode) -> int:
      if not root:
        return 0
      
      s = root.val + iterate(root.left) + iterate(root.right)
      subtrees.add(s)
      
      return s
    
    total = root.val + iterate(root.left) + iterate(root.right)
    ans = 0
    
    for n in subtrees:
      ans = max(ans, (total-n)*n)
      
    return ans % (10**9+7)
    