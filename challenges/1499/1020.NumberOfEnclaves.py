'''
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:

Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
'''


from typing import List


class Solution:
  def numEnclaves(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    seen = set()
    
    def mark(x, y):
      if (x, y) in seen:
        return
        
      stack = [(x, y)]
      while stack:
        x, y = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] == 0:
            continue
            
          if (x0, y0) not in seen:
            stack.append((x0, y0))
            seen.add((x0, y0))
    
    for i in range(m):
      if i == 0 or i == m-1:
        for j in range(n):
          if grid[i][j] == 1:
            mark(i, j)
          
      else:
        if grid[i][0] == 1:
          mark(i, 0)
          
        if grid[i][n-1] == 1:
          mark(i, n-1)
          
    cnt = 0
    for i in range(1, m-1):
      for j in range(1, n-1):
        if grid[i][j] == 1 and (i, j) not in seen:
          cnt += 1
          
    return cnt
    
    
  def numEnclaves(self, grid: List[List[int]]) -> int:
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    m, n = len(grid), len(grid[0])
    
    def mark(i: int, j: int):
      if not grid[i][j]:
        return 0
        
      q = [(i, j)]
      count = 0
      
      while q:
        x, y = q.pop()
        grid[x][y] = 0
        count += 1
        
        for dx, dy in dirs:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or not grid[x0][y0]:
            continue
            
          q.append((x0, y0))
      
      return count
        
    for i in range(m):
      mark(i, 0)
      mark(i, n-1)
      
    for j in range(n):
      mark(0, j)
      mark(m-1, j)
      
    # print('init board:')
    # for r in grid:
    #   print(r)
      
    count = 0
    for i in range(1, m-1):
      for j in range(1, n-1):
        if not grid[i][j]:
          continue
          
        count += 1
        
#     print('final board')
#     for r in grid:
#       print(r)
      
    return count
  