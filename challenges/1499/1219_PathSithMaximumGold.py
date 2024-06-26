'''
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
'''

from typing import List

class Solution:
  def getMaximumGold(self, grid: List[List[int]]) -> int:
    seen = set()
    m, n = len(grid), len(grid[0])
    
    def dfs(x0: int, y0: int):
      gold = 0
      seen.add((x0, y0))
      
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x1 = x0 + dx
        y1 = y0 + dy
        if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
          continue
          
        if (x1, y1) in seen or grid[x1][y1] == 0:
          continue
          
        gold = max(gold, dfs(x1, y1))
      
      seen.discard((x0, y0))
        
      return gold + grid[x0][y0]
    
    max_gold = 0
    for x in range(m):
      for y in range(n):
        if not grid[x][y]:
          continue
        
        max_gold = max(max_gold, dfs(x, y))
        
    return max_gold
        
  def getMaximumGold(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = set()
    most = 0

    def count_degree(x, y):
      c = 0
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] == 0:
          continue
        
        c += 1

      return c
    
    def walk(x, y):
      nonlocal most 
      if not grid[x][y]:
        return 0
        
      gold = 0
      visited.add((x, y))
      
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] == 0 or (x0, y0) in visited:
          continue
          
        gold = max(gold, walk(x0, y0))
                
      curr = grid[x][y]+gold
      most = max(most, curr) 
      visited.discard((x, y))
      
      return curr
    
    for i in range(m):
      for j in range(n):
        if not grid[i][j]:
          continue
          
        if count_degree(i, j) < 3:
          walk(i, j)
        
    return most
    