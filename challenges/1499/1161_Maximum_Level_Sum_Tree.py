'''
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
'''

from typing import Optional
from collections import defaultdict
import math


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    sums = defaultdict(int)
    
    def add(root, level):
      if not root:
        return
      
      sums[level] += root.val
      add(root.left, level+1)
      add(root.right, level+1)
      
    add(root, 1)
    max_val = -math.inf
    ans = 0
    
    for l, s in sums.items():
      if s > max_val:
        max_val = s
        ans = l
      
    return ans  
    