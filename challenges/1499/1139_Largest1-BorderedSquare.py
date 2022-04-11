'''
Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Example 2:

Input: grid = [[1,1,0,0]]
Output: 1

Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1
'''

from typing import List


class Solution:
  def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    rows = [[grid[i][j] for j in range(n)] for i in range(m)]
    cols = [[grid[i][j] for j in range(n)] for i in range(m)]
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 0:
          continue
          
        if j > 0:
          rows[i][j] += rows[i][j-1]
          
        if i > 0:
          cols[i][j] += cols[i-1][j]
          
    # print(rows, cols)
    area = 0
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 0:
          continue
          
        area = max(area, 1)
        k = 1
        
        while i-k >= 0 and j-k >= 0 and grid[i][j-k] == 1 and grid[i-k][j] == 1:
          if cols[i][j-k] >= k+1 and rows[i-k][j] >= k+1:
            area = max(area, (k+1)*(k+1))
            # print(i, j, k)
            
          k += 1
            
    return area
  