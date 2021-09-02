'''
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:

Input: n = 1
Output: [[1]]

Constraints:

1 <= n <= 8
'''


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    lst = [i for i in range(1, n+1)]
    
    def treeish(src: List[int]) -> List[Optional[TreeNode]]:
      if not src:
        return [None]
      
      if len(src) == 1:
        return [TreeNode(src[0])]

      ans = []
      for n in range(len(src)):
        l = treeish(src[:n])
        r = treeish(src[n+1:])
        
        for ln in l:
          for rn in r:
            ans.append(TreeNode(src[n], left=ln, right=rn))
      
      return ans
      
    return treeish(lst)
    