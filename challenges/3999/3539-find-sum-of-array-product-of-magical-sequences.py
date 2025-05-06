'''
3539-find-sum-of-array-product-of-magical-sequences
'''

from math import comb
from functools import cache
from typing import List


class Solution:
  def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
    mod = 10**9 + 7

    @cache
    def dp(m: int, k: int, i: int, flag: int) -> int:
      if m < 0 or k < 0 or m+flag.bit_count() < k:
        return 0

      if m == 0:
        return 1 if k == flag.bit_count() else 0

      if i >= len(nums):
        return 0

      res = 0
      for c in range(m+1):
        mult = (comb(m, c) * pow(nums[i], c, mod)) % mod
        nxt_flag = flag + c
        res += mult * dp(m-c, k-(nxt_flag % 2), i+1, nxt_flag//2)

      return res % mod

    return dp(m, k, 0, 0)
