'''
4009-minimum-possible-maximum-waiting-time
'''

from typing import List
from functools import cache


class Solution:
  def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
    n = len(demand)

    @cache
    def dfs(i: int, f0: int, f1: int, w0: int, w1: int):
      if i >= n:
        return [0, 0]

      res0 = 0
      res1 = 0
      c0 = 0
      c1 = 0
      d = demand[i]

      # use pump 0
      if f0 >= d:
        c0, res0 = dfs(i+1, f0-d, f1, d, max(0, w1-w0))
        res0 = max(res0, w0)
        c0 += 1

      # use pump 1
      if f1 >= d:
        c1, res1 = dfs(i+1, f0, f1-d, max(0, w0-w1), d)
        res1 = max(res1, w1)
        c1 += 1

      # choose the pump that can serve more cars
      if c0 < c1:
        return c1, res1

      if c0 > c1:
        return c0, res0

      return c0, min(res0, res1)

    c, res = dfs(0, fuel[0], fuel[1], 0, 0)

    return res if c else -1


        