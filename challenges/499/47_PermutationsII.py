'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''


from typing import List
from functools import lru_cache


class Solution:
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    
    @lru_cache(None)
    def perm(i: int, mask: int):
      if i >= n:
        return [tuple()]
      
      res = []
      lead_num = set()
      
      for j in range(n):
        if mask & (1<<j) > 0 or nums[j] in lead_num:
          continue
          
        lead_num.add(nums[j])
        for tup in perm(i+1, mask | (1 << j)):
          res.append((nums[j], ) + tup)
          
      return res
      
    return perm(0, 0)
    