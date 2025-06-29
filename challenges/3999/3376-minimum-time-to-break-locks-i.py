'''
3376-minimum-time-to-break-locks-i
'''

from math import ceil
from functools import cache
from typing import List


class Solution:
  def findMinimumTime(self, strength: List[int], k: int) -> int:
    n = len(strength)
    tgt = (1<<n) - 1

    @cache
    def dp(x: int, mask: int) -> int:
      if mask >= tgt:
        return 0

      time = float('inf')
      for i in range(n):
        # already opened
        if (1<<i) & mask > 0:
          continue

        t0 = ceil(strength[i]/x)
        nxt_mask = mask | (1<<i)
        time = min(time, t0+dp(x+k, nxt_mask))

      return time

    return dp(1, 0)
        