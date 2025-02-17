'''
3459-length-of-longest-v-shaped-diagonal-segment
'''

from functools import cache
from typing import List


class Solution:
  def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dirs = [
      (-1, -1),
      (-1, 1),
      (1, 1),
      (1, -1),
    ]

    @cache
    def dp(x: int, y: int, val: int, d: int, turned: bool) -> int:
      if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != val:
        return 0

      d1 = (d+1)%4
      dx0, dy0 = dirs[d]
      dx1, dy1 = dirs[d1]
      l0 = dp(x+dx0, y+dy0, 2-val, d, turned)
      l1 = 0 if turned else dp(x+dx1, y+dy1, 2-val, d1, True)

      return 1+max(l0, l1)

    long = 0
    # print('init:', m, n)

    for x in range(m):
      for y in range(n):
        if grid[x][y] != 1:
          continue

        for i, (dx, dy) in enumerate(dirs):
          # print('run:', (x, y), (i, dx, dy))
          long = max(long, 1+dp(x+dx, y+dy, 2, i, False))

    return long

        