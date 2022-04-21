'''
Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

Example 1:

Input: root = [5,2,-3]
Output: [2,-3,4]
Example 2:

Input: root = [5,2,-5]
Output: [2]

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
'''

from typing import Optional, List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
    sums = defaultdict(int)
    
    def subtree_sum(root):
      if not root:
        return 0
      
      ls, rs = subtree_sum(root.left), subtree_sum(root.right)
      curr_sum = ls + root.val + rs
      sums[curr_sum] += 1
      
      return curr_sum
    
    subtree_sum(root)
    ans = []
    max_count = 0 
    
    for s, c in sums.items():
      if c > max_count:
        max_count = c
        ans.clear()
        ans.append(s)
      
      elif c == max_count:
        ans.append(s)
        
    return ans
    