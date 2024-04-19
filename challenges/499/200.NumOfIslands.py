'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

from typing import List

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    label = [[0]*n for _ in range(m)]
    
    def mark(x: int, y: int, l: int):
      stack = [(x, y)]
      
      while stack:
        x0, y0 = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x1, y1 = x0+dx, y0+dy
          if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
            continue
            
          if grid[x1][y1] == '0' or label[x1][y1] > 0:
            continue
            
          label[x1][y1] = l
          stack.append((x1, y1))
        
    curr_label = 1
    for x in range(m):
      for y in range(n):
        if grid[x][y] == '0' or label[x][y] > 0:
          continue
          
        mark(x, y, curr_label)
        curr_label += 1
        
    return curr_label - 1
     
  def numIslands(self, grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    count = 0
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == '0':
          continue
          
        stack = [(i, j)]
        count += 1
        
        while stack:
          x, y = stack.pop()
          grid[x][y] = '0'
          
          for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x0, y0 = x+dx, y+dy
            if x0 < 0 or x0 >= m or y0 < 0 or y0 >=n or grid[x0][y0] == '0':
              continue
              
            stack.append((x0, y0))
            
    return count
  