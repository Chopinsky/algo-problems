'''
2617. Minimum Number of Visited Cells in a Grid

You are given a 0-indexed m x n integer matrix grid. Your initial position is at the top-left cell (0, 0).

Starting from the cell (i, j), you can move to one of the following cells:

Cells (i, k) with j < k <= grid[i][j] + j (rightward movement), or
Cells (k, j) with i < k <= grid[i][j] + i (downward movement).
Return the minimum number of cells you need to visit to reach the bottom-right cell (m - 1, n - 1). If there is no valid path, return -1.

Example 1:

Input: grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
Output: 4
Explanation: The image above shows one of the paths that visits exactly 4 cells.
Example 2:

Input: grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
Output: 3
Explanation: The image above shows one of the paths that visits exactly 3 cells.
Example 3:

Input: grid = [[2,1,0],[1,0,0]]
Output: -1
Explanation: It can be proven that no path exists.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10^5
1 <= m * n <= 10^5
0 <= grid[i][j] < m * n
grid[m - 1][n - 1] == 0
'''

import math
from typing import List
from heapq import heappush, heappop


class Solution:
  def minimumVisitedCells(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    if m == 1 and n == 1:
      return 1
    
    cols = [[] for _ in range(n)]
    cols[0].append((1, 0, 0))
    row = []
    
    def is_valid(x0, y0, x1, y1):
      if x0 == x1:
        return y0+grid[x0][y0] >= y1
      
      if y0 == y1:
        return x0+grid[x0][y0] >= x1
        
      return False
    
    def get_cells(row, col):
      cells = math.inf
      if row:
        cells = min(row[0][0]+1, cells)

      if col:
        cells = min(col[0][0]+1, cells)

      return cells if cells < math.inf else -1
    
    for x in range(m):
      row.clear()
      if x == 0:
        heappush(row, (1, 0, 0))
      else:
        while cols[0] and not is_valid(cols[0][0][1], cols[0][0][2], x, 0):
          heappop(cols[0])
          
        if cols[0]:
          cells = cols[0][0][0] + 1
          heappush(cols[0], (cells, x, 0))
          heappush(row, (cells, x, 0))
          # print('reach:', (x, 0), cells)
          
          if x == m-1 and n == 1:
            return get_cells([], cols[0])
          
      for y in range(1, n):
        while row and not is_valid(row[0][1], row[0][2], x, y):
          heappop(row)
          
        while cols[y] and not is_valid(cols[y][0][1], cols[y][0][2], x, y):
          heappop(cols[y])
          
        if x == m-1 and y == n-1:
          return get_cells(row, cols[y])
        
        if grid[x][y] == 0:
          continue
        
        cells = get_cells(row, cols[y])
        if cells > 0:
          # print('reach:', (x, y), cells)
          heappush(row, (cells, x, y))
          heappush(cols[y], (cells, x, y))
    
    return -1
    