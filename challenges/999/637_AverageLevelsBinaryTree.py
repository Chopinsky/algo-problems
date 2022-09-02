'''
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    sums = []
    count = []
    
    def iterate(root, lvl):
      if not root:
        return 
      
      if lvl >= len(sums):
        sums.append(root.val)
        count.append(1)
      else:
        sums[lvl] += root.val
        count[lvl] += 1
        
      iterate(root.left, lvl+1)
      iterate(root.right, lvl+1)
      
    iterate(root, 0)
    
    return [s/c for s, c in zip(sums, count)]
    