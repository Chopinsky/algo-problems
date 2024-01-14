'''
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Example 1:

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:

Input: root = [1,null,2,null,0,3]
Output: 3

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 10^5
'''

from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    ans = 0
    
    def walk(root):
      nonlocal ans
      if not root:
        return None

      val = root.val
      rng = [val, val]

      l = walk(root.left)
      if l:
        ans = max(ans, abs(val - l[0]), abs(val - l[1]))
        rng[0] = min(rng[0], l[0])
        rng[1] = max(rng[1], l[1])
        
      r = walk(root.right)
      if r:
        ans = max(ans, abs(val - r[0]), abs(val - r[1]))
        rng[0] = min(rng[0], r[0])
        rng[1] = max(rng[1], r[1])
      
      return rng
    
    walk(root)
    
    return ans
        

  def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    def dive(root, s, b):
      if not root:
        return 0
      
      score = max(abs(root.val - s), abs(root.val - b))
      s = min(s, root.val)
      b = max(b, root.val)
      
      return max(score, dive(root.left, s, b), dive(root.right, s, b))
      
    return max(dive(root.left, root.val, root.val), dive(root.right, root.val, root.val))

    
  def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    max_diff = 0
    
    def walk(root: Optional[TreeNode], rng: Tuple[int, int]):
      nonlocal max_diff
      
      if not root:
        return
      
      max_diff = max(max_diff, abs(root.val - rng[0]), abs(root.val - rng[1]))
      
      walk(root.left, (min(root.val, rng[0]), max(root.val, rng[1])))
      walk(root.right, (min(root.val, rng[0]), max(root.val, rng[1])))
      
    walk(root, (root.val, root.val))
    
    return max_diff
  