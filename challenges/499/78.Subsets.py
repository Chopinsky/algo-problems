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
from itertools import combinations
from functools import lru_cache

class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    
    @lru_cache(None)
    def gen(i: int):
      if i >= n:
        return tuple([tuple()])
      
      result = list(gen(i+1))
      rest = [list(t) for t in result]
      val = nums[i]
      # print('gen:', i, val, rest)
      
      for lst in rest:
        # print('iter:', lst)
        result.append(tuple([val] + lst))
        
      return tuple(result)
    
    return gen(0)
        
  def subsets(self, nums: List[int]) -> List[List[int]]:
    ans = [[]]
    n = len(nums)
    
    for l in range(1, n+1):
      for sub in combinations(nums, l):
        ans.append(sub)
        
    return ans
  