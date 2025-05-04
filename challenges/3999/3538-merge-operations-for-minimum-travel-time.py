'''
3538-merge-operations-for-minimum-travel-time
'''

import math
from functools import cache
from typing import List


class Solution:
  def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
    @cache
    def dp(idx, speed, extra, prev, rem: int):
      if idx == n-1:
        return (l-prev) * speed if rem == 0 else math.inf

      cost = speed * (position[idx] - prev)
      take = cost + dp(idx+1, time[idx]+extra, 0, position[idx], rem)

      if rem == 0:
        return take

      # merge
      not_take = dp(idx+1, speed, time[idx]+extra, prev, rem-1)
      return min(take, not_take)

    return dp(1, time[0], 0, 0, k)
