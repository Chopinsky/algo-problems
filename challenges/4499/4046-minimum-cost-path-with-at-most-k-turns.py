'''
4046-minimum-cost-path-with-at-most-k-turns
'''

from functools import cache
from heapq import heappop, heappush
from math import inf


class Solution:
  def minCost0(self, grid: list[list[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if m > 1 and n > 1 and k == 0:
      return -1

    @cache
    def dp(x0: int, y0: int, d0: int, k0: int) -> int:
      if x0 == m-1 and y0 == n-1:
        return grid[x0][y0]

      res = inf
      for d1, (dx, dy) in enumerate(d):
        x1, y1 = x0+dx, y0+dy
        if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
          continue

        k1 = k0 - (d0 != d1)
        if k1 < 0:
          continue

        res = min(res, dp(x1, y1, d1, k1))

      return res + grid[x0][y0]

    return min(dp(0, 0, 0, k), dp(0, 0, 1, k))

  def minCost(self, grid: list[list[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    dp = [[[[inf]*4 for _ in range(k+1)] for _ in range(n)] for _ in range(m)]
    cand = [(grid[0][0], 0, 0, 0, 0), (grid[0][0], 0, 0, 0, 1)]

    for i in range(4):
      dp[0][0][0][i] = grid[0][0]

    while cand:
      c0, x0, y0, t0, d0 = heappop(cand)
      if c0 > dp[x0][y0][t0][d0]:
        # handled elsewhere 
        continue

      if x0 == m-1 and y0 == n-1:
        break

      for d1, (dx, dy) in enumerate(d):
        x1, y1 = x0+dx, y0+dy       
        if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
          # out of the grid
          continue

        t1 = t0 + (0 if d1 == d0 else 1)
        if t1 > k:
          # making more turns than allowed
          continue

        c1 = c0 + grid[x1][y1]
        if c1 >= dp[x1][y1][t1][d1]:
          # better solution exists
          continue

        if t1 > 0 and c1 >= dp[x1][y1][t1-1][d1]:
          # should not cost more with more turns
          continue

        dp[x1][y1][t1][d1] = c1
        heappush(cand, (c1, x1, y1, t1, d1))
        # print('push:', (c1, x1, y1, t1, d1), dp[x1][y1])

    res = min(min(dp[m-1][n-1][tt][dd] for dd in range(4)) for tt in range(k+1))
    return res if res < inf else -1
        