'''
983. Minimum Cost For Tickets
'''

from bisect import bisect_left
from functools import lru_cache
from typing import List


class Solution:
  def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    n = len(days)

    @lru_cache(None)
    def dp(i: int):
      if i >= n:
        return 0

      day = days[i]
      i1 = i + 1
      c1 = costs[0] + dp(i1)

      i2 = bisect_left(days, day+7)
      c2 = costs[1] + dp(i2)

      i3 = bisect_left(days, day+30)
      c3 = costs[2] + dp(i3)
      
      return min(c1, c2, c3)
      
    return dp(0)
        