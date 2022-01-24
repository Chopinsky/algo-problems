'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''


from typing import List


class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    stack, nxt = [], []
    m, n = len(grid), len(grid[0])
    total = 0
    
    for i in range(m):
      for j in range(n):
        if not grid[i][j]:
          continue
          
        total += 1
        if grid[i][j] == 2:
          stack.append((i, j))
        
    if not stack:
      return 0 if not total else -1
    
    step = 0
    bad = len(stack)
    
    while stack:
      step += 1
      for x, y in stack:
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
          x0, y0 = x+dx, y+dy
          if 0 <= x0 < m and 0 <= y0 < n and grid[x0][y0] == 1:
            nxt.append((x0, y0))
            grid[x0][y0] = 2
            bad += 1
      
      stack, nxt = nxt, stack
      # print(step, stack)
      nxt.clear()
  
    if bad < total:
      return -1
      
    return step-1
  