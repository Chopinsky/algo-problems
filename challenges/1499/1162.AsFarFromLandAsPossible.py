'''
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Example 1:

Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:

Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''

from typing import List
import math


class Solution:
  def maxDistance(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dist = [[math.inf]*n for _ in range(m)]
    curr, nxt = set(), set()
    max_dist = -1
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          curr.add((i, j))
          dist[i][j] = 0
          
    # print(curr)
    
    while curr:
      for x, y in curr:
        d = dist[x][y]
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x0, y0 = x+dx, y+dy
          
          # out of bound
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
            continue
            
          # not a water, or not to a closer land
          if grid[x0][y0] != 0 or d+1 >= dist[x0][y0]:
            continue
            
          dist[x0][y0] = d+1
          nxt.add((x0, y0))
          
      curr, nxt = nxt, curr
      nxt.clear()
    
    # print(dist)
    for x in range(m):
      for y in range(n):
        if dist[x][y] != math.inf and dist[x][y] > 0:
          max_dist = max(max_dist, dist[x][y])
    
    return max_dist
  

  def maxDistance(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    stack, nxt = [], []
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          stack.append((i, j))
          
    if not stack or len(stack) == m*n:
      return -1
    
    dist = 0
    seen = set()
    
    while stack:
      # print(dist, stack)
      
      for x, y in stack:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
            continue
            
          if grid[x0][y0] == 1 or (x0, y0) in seen:
            continue
            
          nxt.append((x0, y0))
          seen.add((x0, y0))
            
      stack, nxt = nxt, stack
      nxt.clear()
      dist += 1
      
    return dist-1
  