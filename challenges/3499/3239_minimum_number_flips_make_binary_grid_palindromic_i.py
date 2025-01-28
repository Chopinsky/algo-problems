'''
3239. minimum-number-of-flips-to-make-binary-grid-palindromic-i
'''

from typing import List


class Solution:
  def minFlips(self, grid: List[List[int]]) -> int:
    ch, cv = 0, 0
    m, n = len(grid), len(grid[0])

    # flip for rows
    for x in range(m):
      y0, y1 = 0, n-1
      while y0 < y1:
        if grid[x][y0] != grid[x][y1]:
          ch += 1

        y0 += 1
        y1 -= 1

    # flip for cols
    for y in range(n):
      x0, x1 = 0, m-1
      while x0 < x1:
        if grid[x0][y] != grid[x1][y]:
          cv += 1

        x0 += 1
        x1 -= 1

    # print('done:', ch, cv)
    return min(ch, cv)
        