'''
3509-maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k
'''

from functools import cache
from typing import List


class Solution:
  def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
    n = len(nums)

    @cache
    def dp(i: int, sign: int, sums: int, prod: int, is_empty: int) -> int:
      if i >= n:
        if is_empty == 0 and sums == k and prod <= limit:
          return prod

        return -1

      val = nums[i]
      return max(
        # not use this number
        dp(i+1, sign, sums, prod, is_empty),
        # use this number
        dp(i+1, -1*sign, sums+sign*val, min(limit+1, prod*val), 0)
      )
      
    ans = dp(0, 1, 0, 1, 1)
    dp.cache_clear()
    return ans
         