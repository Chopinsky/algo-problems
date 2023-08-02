'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

from functools import lru_cache
from typing import List, Tuple


class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    @lru_cache(None)
    def dp(src: Tuple) -> List:
      res = []
      
      if len(src) == 1:
        res.append(src)
        return res
      
      if len(src) == 2:
        a, b = src
        res.append((a, b))
        res.append((b, a))
        return res
      
      for i in range(len(src)):
        nxt = tuple(src[:i] + src[i+1:])
        val = src[i]
        
        for t in dp(nxt):
          res.append((val, ) + t)
      
      return res
    
    return dp(tuple(nums))
    

  def permute(self, nums: List[int]) -> List[List[int]]:
    comb, ans = [], []
    n = len(nums)
    added = set()
    
    def perm(i: int):
      if i == n:
        ans.append(list(comb))
        return
      
      for j in range(n):
        if j in added:
          continue
          
        added.add(j)
        comb.append(nums[j])
        
        perm(i+1)
      
        added.discard(j)
        comb.pop()
      
    perm(0)
    
    return ans
  