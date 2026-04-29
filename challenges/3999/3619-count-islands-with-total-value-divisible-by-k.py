'''
3619-count-islands-with-total-value-divisible-by-k
'''

from typing import List
from collections import deque


class Solution:
  def countIslands(self, grid: List[List[int]], k: int) -> int:
    m = len(grid)
    n = len(grid[0])
    count = 0
    seen = set()

    def get_island(x: int, y: int) -> bool:
      q = deque([(x, y)])
      seen.add((x, y))
      score = grid[x][y]

      while q:
        x0, y0 = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
          x1, y1 = x0+dx, y0+dy
          if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
            continue

          if grid[x1][y1] == 0:
            continue

          if (x1, y1) in seen:
            continue

          seen.add((x1, y1))
          q.append((x1, y1))
          score += grid[x1][y1]

      return score % k == 0

    for x in range(m):
      for y in range(n):
        if grid[x][y] == 0:
          continue

        if (x, y) in seen:
          continue

        if get_island(x, y):
          count += 1

    return count
  