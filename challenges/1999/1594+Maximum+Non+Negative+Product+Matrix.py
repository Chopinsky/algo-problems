'''
1594. Maximum Non Negative Product in a Matrix

You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.

Notice that the modulo is performed after getting the maximum product.

Example 1:


Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
Example 2:


Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
Example 3:

Input: grid = [[1,3],[0,-4]]
Output: 0
Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
-4 <= grid[i][j] <= 4
'''

from typing import List

class Solution:
  def maxProductPath(self, grid: List[List[int]]) -> int:
    inf = float('inf')
    cell = [inf, inf]
    mod = 10**9 + 7
    
    if grid[0][0] >= 0:
      cell[0] = grid[0][0]
    else:
      cell[1] = grid[0][0]
      
    curr, nxt = [cell], []
    w = len(grid[0])
    has_zero = grid[0][0] == 0
    
    def update_prod(cell, prod):
      if prod < 0:
        cell[1] = prod if cell[1] == inf else min(cell[1], prod)
      else:
        cell[0] = prod if cell[0] == inf else max(cell[0], prod)
        
      return cell
      
    def update(prev, cell, val):
      if prev[0] != inf:
        cell = update_prod(cell, prev[0]*val)
        
      if prev[1] != inf:
        cell = update_prod(cell, prev[1]*val)
          
      return cell
    
    for c in range(1, w):
      has_zero |= grid[0][c] == 0
      cell = update(curr[-1], [inf, inf], grid[0][c])
      curr.append(cell)
      
    # print('init:', curr)
    for row in grid[1:]:
      for c in range(w):
        has_zero |= row[c] == 0
        cell = update(curr[c], [inf, inf], row[c])
        if c > 0:
          cell = update(nxt[-1], cell, row[c])
          
        nxt.append(cell)
      
      # print('row:', row, nxt)
      curr, nxt = nxt, curr
      nxt.clear()
      
    last = curr[-1]
    if last[0] == inf:
      return 0 if has_zero else -1
    
    return last[0]%mod
        