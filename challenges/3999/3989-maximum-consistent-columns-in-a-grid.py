'''
3989-maximum-consistent-columns-in-a-grid
'''

from typing import List
from collections import defaultdict
from functools import cache


class Solution:
  def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
    m = len(grid)
    n = len(grid[0])
    nb = defaultdict(list)

    def has_conn(y0: int, y1: int) -> bool:
      for x in range(m):
        if abs(grid[x][y0] - grid[x][y1]) > limit:
          return False

      return True

    for y0 in range(1, n):
      for y1 in range(y0):
        if has_conn(y0, y1):
          nb[y1].append(y0)

    # print('init:', nb)

    @cache
    def dfs(u: int) -> int:
      if not nb[u]:
        return 1

      cnt = max(dfs(v) for v in nb[u])
      return 1+cnt
      
    return max(dfs(u) for u in range(n))
        