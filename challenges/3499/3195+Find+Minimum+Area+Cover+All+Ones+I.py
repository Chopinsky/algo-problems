'''
3195. Find the Minimum Area to Cover All Ones I
'''

from typing import List

class Solution:
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
        