'''
3444-minimum-increments-for-target-multiples-in-an-array
'''

from typing import List
from functools import cache


class Solution:
  def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
    n = len(nums)
    m = len(target)
    done_mask = (1<<m)-1

    @cache
    def get_lcm(mask: int) -> int:
      val = 0
      curr = 1
      idx = 0

      while curr <= mask:
        if curr&mask > 0:
          val = target[idx] if val == 0 else lcm(val, target[idx])

        idx += 1
        curr <<= 1

      return val

    def get_mask(val: int) -> int:
      m0 = 0
      for i in range(m):
        if val % target[i] == 0:
          m0 |= (1 << i)

      return m0

    @cache
    def dp(i: int, mask: int) -> int:
      if mask == done_mask:
        return 0

      cost = float('inf')
      if i >= n:
        return cost

      val = nums[i]
      for m0 in range(done_mask+1):
        # don't update this number
        if m0 == 0:
          m1 = get_mask(val)
          cost = min(cost, dp(i+1, mask|m1))
          continue

        # overlapped contributions
        if m0&mask != 0:
          continue

        lcm_val = get_lcm(m0)
        if lcm_val >= val:
          base_cost = lcm_val - val
        else:
          base_cost = lcm_val - (val%lcm_val)

        cost = min(cost, base_cost+dp(i+1, mask|m0))

      return cost
      
    return dp(0, 0)
        