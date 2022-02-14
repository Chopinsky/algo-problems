'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''


from typing import List
from functools import lru_cache


class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    
    @lru_cache(None)
    def dp(i: int, m: int) -> List[List[int]]:
      if m == 0 or i >= n:
        return [[]]
        
      if n-i == m:
        return [nums[i:]]
      
      res = []
      for j in range(i, min(n, n-m+1)):
        for subarr in dp(j+1, m-1):
          res.append([nums[j]] + subarr)
      
      return res
      
    ans = []
    for ln in range(n+1):
      ans += dp(0, ln)
    
    return ans
  