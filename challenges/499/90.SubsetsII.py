'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

from typing import List
from collections import defaultdict
from itertools import combinations


class Solution:
  def subsetsWithDup0(self, nums: List[int]) -> List[List[int]]:
    ans = [[]]
    n = len(nums)
    nums = sorted(nums)
    base = [i for i in range(n)]
    seen = set()
    
    for l in range(1, n+1):
      for sub in combinations(base, l):
        arr = [nums[i] for i in sub]
        if tuple(arr) in seen:
          continue
          
        ans.append(arr)
        seen.add(tuple(arr))
        
    return ans

  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    if not len(nums):
      return []
    
    nums = sorted(nums)
    var = defaultdict(int)
    ans = [[]]
    batch = []
    
    for i, n0 in enumerate(nums):
      var[n0] += 1
      if i > 0 and n0 != nums[i-1]:
        ans += batch
        batch = []
        
      base = [n0] * var[n0]
      for src in ans:
        batch.append(src + base)

    ans += batch
    
    return ans
  