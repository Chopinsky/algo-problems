'''
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

Example 1:

Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.
Example 2:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10^5
2 <= m * n <= 10^5
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
'''

from typing import List
from heapq import heappush, heappop
import math


class Solution:
  def minimumObstacles(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    removes = [[math.inf]*n for _ in range(m)]
    removes[0][0] = 1 if grid[0][0] == 1 else 0
    # seen = set([(0, 0)])
    stack = [(removes[0][0], 0, 0)]
    
    while stack:
      _, x0, y0 = heappop(stack)
      val = removes[x0][y0]
      
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x1, y1 = x0+dx, y0+dy
        if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
          continue
        
        nxt_val = val + grid[x1][y1]
        if nxt_val >= removes[x1][y1]:
          continue
          
        removes[x1][y1] = nxt_val
        heappush(stack, (nxt_val, x1, y1))
        
    return removes[m-1][n-1]
    
  def minimumObstacles(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    removes = [[math.inf]*n for _ in range(m)]
    stack = [(grid[0][0], 0, 0)]
    removes[0][0] = grid[0][0]
    
    while stack:
      # print(stack)
      cnt, x, y = heappop(stack)
      if x == m-1 and y == n-1:
        return cnt
      
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
          continue
          
        nxt_cnt = cnt + grid[x0][y0]
        if nxt_cnt >= removes[x0][y0]:
          continue
          
        removes[x0][y0] = nxt_cnt
        heappush(stack, (nxt_cnt, x0, y0))
    
    return m * n
  