'''
3286. Find a Safe Walk Through a Grid
'''

from heapq import heappush, heappop
from typing import List


class Solution:
  def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
    m, n = len(grid), len(grid[0])
    h = [[0]*n for _ in range(m)]
    h[0][0] = health - grid[0][0]
    
    if h[0][0] <= 0:
      return False
    
    stack = [(-h[0][0], 0, 0)]
    while stack:
      _, x0, y0 = heappop(stack)
      h0 = h[x0][y0]
      
      if h0 == 0:
        continue
        
      if x0 == m-1 and y0 == n-1:
        return True
      
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x1, y1 = x0+dx, y0+dy
        if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
          continue
          
        h1 = h0 - grid[x1][y1]
        if h1 <= h[x1][y1]:
          continue
          
        h[x1][y1] = h1
        heappush(stack, (-h1, x1, y1))
    
    return False
  