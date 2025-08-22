'''
3195. Find the Minimum Area to Cover All Ones I
'''

from typing import List


class Solution:
  def minimumArea(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    lx, rx = m, -1
    uy, by = n, -1

    for x in range(m):
      for y in range(n):
        if grid[x][y] == 0:
          continue

        lx = min(lx, x)
        rx = max(rx, x)
        uy = min(uy, y)
        by = max(by, y)

    # print('done:', lx, rx, uy, by)
    return (rx-lx+1) * (by-uy+1)
        
  def minimumArea(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    left = n
    right = 0
    top = m
    bottom = 0
    
    for x in range(m):
      for y in range(n):
        if grid[x][y] == 0:
          continue
          
        left = min(left, y)
        right = max(right, y)
        top = min(top, x)
        bottom = max(bottom, x)
        
    return (right-left+1) * (bottom-top+1)
        