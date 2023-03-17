'''
2556. Disconnect Path in a Binary Matrix by at Most One Flip

You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1) that has the value 1. The matrix is disconnected if there is no path from (0, 0) to (m - 1, n - 1).

You can flip the value of at most one (possibly none) cell. You cannot flip the cells (0, 0) and (m - 1, n - 1).

Return true if it is possible to make the matrix disconnect or false otherwise.

Note that flipping a cell changes its value from 0 to 1 or from 1 to 0.

Example 1:

Input: grid = [[1,1,1],[1,0,0],[1,1,1]]
Output: true
Explanation: We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.
Example 2:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: false
Explanation: It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 10^5
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 1
'''

from typing import List


class Solution:
  def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
    m, n = len(grid), len(grid[0])
    if m == 1 or n == 1:
      if (m == 1 and n <= 2) or (n == 1 and m <= 2):
        return False
      
      return True
    
    if grid[m-1][n-2] != 1 or grid[m-2][n-1] != 1:
      return True
    
    if grid[0][1] != 1 or grid[1][0] != 1:
      return True
    
    def dfs(seen):
      stack = [(0, 0, 0)]
      while stack and (stack[-1][0] != m-1 or stack[-1][1] != n-1):
        x, y, state = stack.pop()
        if state == 2:
          continue

        if state == 0:
          x0, y0 = x+1, y
          stack.append((x, y, 1))
        else:
          x0, y0 = x, y+1
          stack.append((x, y, 2))

        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] != 1 or (x0, y0) in seen:
          continue

        stack.append((x0, y0, 0))
      
      if not stack or (stack[-1][0] != m-1 and stack[-1][1] != n-1):
        return set()

      return set([(x, y) for x, y, _ in stack])
      
    p0 = dfs(set())
    # print('init path points:', p0)
    
    if (m-1, n-1) not in p0:
      return True
    
    p0.discard((m-1, n-1))
    p1 = dfs(p0)
    
    if (m-1, n-1) not in p1:
      return True
    
    return False
  