'''
3469-find-minimum-cost-to-remove-array-elements
'''

from typing import List
from functools import cache


class Solution:
  def minCost(self, nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
      return max(nums)

    @cache
    def dp(i: int, j: int) -> int:
      if i > n:
        return 0

      if i == n:
        return nums[j]

      if i == n-1:
        return max(nums[i], nums[j])
      
      v0 = max(nums[j], nums[i]) + dp(i+2, i+1) # take j, i
      v1 = max(nums[j], nums[i+1]) + dp(i+2, i) # take j, i+1
      v2 = max(nums[i], nums[i+1]) + dp(i+2, j) # take i, i+1

      return min(v0, v1, v2)

    res = dp(1, 0)
    dp.cache_clear()

    return res
        