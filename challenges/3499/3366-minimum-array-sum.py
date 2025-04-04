'''
3366-minimum-array-sum
'''

from typing import List
from functools import cache
import math


class Solution:
  def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
    def calc(val: int) -> int:
      v0 = (val-k+1) // 2
      v1 = (val+1) // 2
      if v1 < k:
        return v0

      return min(v0, v1-k)

    @cache
    def dp(i: int, o1: int, o2: int) -> int:
      if i >= len(nums):
        return 0

      val = nums[i]
      c0 = val + dp(i+1, o1, o2)
      c1 = (val+1)//2 + dp(i+1, o1-1, o2) if o1 > 0 else math.inf
      c2 = val-k + dp(i+1, o1, o2-1) if o2 > 0 and val >= k else math.inf
      if o1 > 0 and o2 > 0 and val >= k:
        c3 = calc(val) + dp(i+1, o1-1, o2-1)
      else:
        c3 = math.inf
      
      return min(c0, c1, c2, c3)

    return dp(0, op1, op2)
