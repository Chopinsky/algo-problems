'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:


Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
'''


from typing import List, Tuple
from collections import deque


class Solution:
  def closedIsland(self, grid: List[List[int]]) -> int:
    seen = set()
    m, n = len(grid), len(grid[0])
    
    def search(x, y):
      seen.add((x, y))
      if grid[x][y] == 1:
        return False
      
      stack = [(x, y)]
      isIsolated = True
      
      while stack:
        x0, y0 = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x1, y1 = x0+dx, y0+dy
          if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
            isIsolated = False
            continue
            
          if (x1, y1) in seen:
            continue
            
          seen.add((x1, y1))
          if grid[x1][y1] == 1:
            continue
            
          stack.append((x1, y1))
        
      return isIsolated
    
    cnt = 0
    for x in range(m):
      for y in range(n):
        if (x, y) in seen:
          continue
          
        if search(x, y):
          cnt += 1
          
    return cnt
        
  
  def closedIsland(self, grid: List[List[int]]) -> int:
    seen = set()
    m, n = len(grid), len(grid[0])
    if m < 3 or n < 3:
      return 0
    
    islands = {}
    
    for i in range(m):
      for j in range(n):
        if (i, j) in seen or grid[i][j] == 1:
          continue
          
        stack = deque([(i, j)])
        root = i*n + j
        islands[root] = True
        seen.add((i, j))
        
        while stack:
          x, y = stack.popleft()
          for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x0, y0 = x+dx, y+dy
            if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
              islands[root] = False
              continue
              
            if grid[x0][y0] == 1 or (x0, y0) in seen:
              continue
              
            stack.append((x0, y0))
            seen.add((x0, y0))
          
    # print(islands)
        
    return sum(1 if islands[k] else 0 for k in islands)
      