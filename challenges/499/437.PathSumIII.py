from typing import Optional, Dict
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def pathSum(self, root: Optional[TreeNode], target: int) -> int:
    def dfs(root: Optional[TreeNode], chain_sum: int):
      nonlocal count

      if not root: 
        return 

      chain_sum += root.val
      
      # the chain from the root till this node yield
      # sum of the target
      if chain_sum == target: 
        count += 1

      # the partial chain sum we're looking for will be:
      #     chain_sum - partial_sum = target
      # hence partial_sum = chain_sum - target
      count += presum[chain_sum - target]
      presum[chain_sum] += 1

      if root.left: 
        dfs(root.left, chain_sum)

      if root.right: 
        dfs(root.right, chain_sum)

      presum[chain_sum] -= 1

    count = 0
    presum = defaultdict(int)
    
    dfs(root, 0)
    
    return count 
 

  def pathSum0(self, root: Optional[TreeNode], target: int) -> int:
    def iterate(root: Optional[TreeNode], curr: Dict[int, int]) -> int:
      if not root:
        return 0
      
      sole = 1 if root.val == target else 0
      tail = curr[target-root.val]
      
      nxt = defaultdict(int)
      nxt[root.val] += 1
      
      for s in curr:
        nxt[s+root.val] += curr[s]
      
      left = iterate(root.left, nxt)
      right = iterate(root.right, nxt)
      
      # if root.val == 3:
      #   print(curr, sole, tail, left, right)
      
      return sole + tail + left + right
      
    return iterate(root, defaultdict(int))
  