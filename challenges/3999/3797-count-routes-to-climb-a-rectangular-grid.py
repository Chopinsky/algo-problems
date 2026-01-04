'''
3797-count-routes-to-climb-a-rectangular-grid
'''

from math import isqrt
from typing import List


class Solution:
  def numberOfRoutes(self, grid: List[str], d: int) -> int:
    m = len(grid[0])
    mod = 10**9 + 7

    def f(dp: List, d: int, r: str) -> List:
      dp2 = [0]*m
      dp2[0] = sum(dp[:d+1]) # move to 0 from prev row

      for j in range(1, m):
        dp2[j] = dp2[j-1]

        if j-d-1 >= 0:
          dp2[j] -= dp[j-d-1]
        
        if j+d < m:
          dp2[j] += dp[j+d]

      for j, c in enumerate(r):
        dp2[j] = 0 if c == '#' else dp2[j]%mod

      return dp2

    dp = None
    for r in grid[::-1]:
      # vertical moves
      if dp is None:
        dp = f([1]*m, 0, r)
      else:
        dp = f(dp, isqrt(d*d-1), r)

      # horizontal moves
      dp = f(dp, d, r)

    return sum(dp)%mod
