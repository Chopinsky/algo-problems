'''
3548-equal-sum-grid-partition-ii
'''

from typing import List


class Solution:
  def canPartitionGrid(self, grid: List[List[int]]) -> bool:
    total = sum(sum(r) for r in grid)
    m, n = len(grid), len(grid[0])

    def check(g):
      seen = set()
      top = 0
      can_remove = len(g[0]) > 1

      for i, row in enumerate(g):
        seen |= set(row)
        top += sum(row)
        bot = total - top
        diff = top - bot
        
        if diff in [0, g[0][0], g[0][-1], g[i][0]]:
          return True

        if can_remove and i > 0 and diff in seen:
          return True
      
      return False

    if check(grid) or check(grid[::-1]):
      return True
        
    # transpose the grid
    grid = list(zip(*grid))
    return check(grid) or check(grid[::-1])
