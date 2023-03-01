'''
2577. Minimum Time to Visit a Cell In a Grid

You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.

Example 1:

Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
Output: 7
Explanation: One of the paths that we can take is the following:
- at t = 0, we are on the cell (0,0).
- at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
- at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
- at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
- at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
- at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
- at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
- at t = 7, we move to the cell (2,3). It is possible because grid[1][3] <= 7.
The final time is 7. It can be shown that it is the minimum time possible.
Example 2:



Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
Output: -1
Explanation: There is no path from the top left to the bottom-right cell.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
0 <= grid[i][j] <= 105
grid[0][0] == 0
'''

from typing import List
from heapq import heappop, heappush


class Solution:
  def minimumTime(self, grid: List[List[int]]) -> int:
    stack = []
    m, n = len(grid), len(grid[0])
    time = {(0, 0): 0}
    
    if n > 1 and grid[0][1] <= 1:
      stack.append((1, 0, 1))
      time[0, 1] = 1
      
    if m > 1 and grid[1][0] <= 1:
      stack.append((1, 1, 0))
      time[1, 0] = 1
      
    if not stack:
      return -1
    
    if len(stack) < 2:
      _, x, y = stack[0]
      x0, y0 = 1-x, 1-y
      t0 = 2*(grid[x0][y0]//2) + 1
      heappush(stack, (t0, x0, y0))
    
    while stack:
      t, x, y = heappop(stack)
      # print('curr:', (x, y), t)
      
      if x == m-1 and y == n-1:
        return t
      
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
          continue
          
        if grid[x0][y0] <= t+1:
          t0 = t+1
        else:
          rnd = (grid[x0][y0] - t) // 2
          t0 = t + 2*rnd + 1
          
        # better solution exists
        if (x0, y0) in time and time[x0, y0] <= t0:
          continue
        
        time[x0, y0] = t0
        # print('from', (x, y), 'to', (x0, y0), 'at', t0)
        heappush(stack, (t0, x0, y0))
      
    # print(time)
    return -1
      