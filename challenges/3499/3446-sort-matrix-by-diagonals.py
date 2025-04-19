'''
3446-sort-matrix-by-diagonals
'''

from typing import List


class Solution:
  def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    if n == 1:
      return grid
    
    for r in range(n-1, -1, -1):
      x, y = r, 0
      vals = []
      while x < n and y < n:
        vals.append(grid[x][y])
        x += 1
        y += 1

      vals.sort()
      x, y = r, 0
      while x < n and y < n and vals:
        grid[x][y] = vals.pop()
        x += 1
        y += 1

    for c in range(1, n):
      x, y = 0, c
      vals = []
      while x < n and y < n:
        vals.append(grid[x][y])
        x += 1
        y += 1

      vals.sort()
      vals = vals[::-1]
      x, y = 0, c
      while x < n and y < n:
        grid[x][y] = vals.pop()
        x += 1
        y += 1
  
    return grid