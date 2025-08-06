'''
3599-partition-array-to-minimize-xor
'''

from functools import cache
from typing import List


class Solution:
  def minXor(self, nums: List[int], k: int) -> int:
    n = len(nums)

    @cache
    def dp(i: int, rem: int) -> int:
      if i >= n or rem <= 0:
        return -1

      if rem == 1:
        curr = 0
        for val in nums[i:]:
          curr ^= val

        return curr

      if n-i == rem:
        return max(nums[i:])

      curr = 0
      res = -1
      # print('iter:', (i, rem))

      for j in range(i, n):
        curr ^= nums[j]
        rest = dp(j+1, rem-1)
        # print('inner:', curr, rest)
        if rest < 0:
          break

        if j == i:
          res = max(curr, rest)
        else:
          res = min(res, max(curr, rest))

      return res

    return dp(0, k)
        