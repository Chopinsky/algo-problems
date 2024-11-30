'''
3341. Find Minimum Time to Reach Last Room I
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  def minTimeToReach(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    stack = [(0, 0, 0)]
    seen = set()
        
    while stack:
      t0, x0, y0 = heappop(stack)
      if (x0, y0) in seen:
        continue
        
      if x0 == m-1 and y0 == n-1:
        return t0
      
      seen.add((x0, y0))
      
      for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        x1, y1 = x0+dx, y0+dy
        if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
          continue
          
        if (x1, y1) in seen:
          continue
          
        t1 = 1+max(t0, grid[x1][y1])
        heappush(stack, (t1, x1, y1))
      
    return -1
    