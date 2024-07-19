'''
3212. Count Submatrices With Equal Frequency of X and Y

Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
 

Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:

Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 'X', 'Y', or '.'.
'''

from typing import List

class Solution:
  def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
    n = len(grid[0])
    prev, curr = [], []
    count = 0
    
    for row in grid:
      xc, yc = 0, 0
      for i in range(n):
        cell = row[i]
        if cell == 'X':
          xc += 1
        
        if cell == 'Y':
          yc += 1
          
        subx = xc + (0 if not prev else prev[i][0])
        suby = yc + (0 if not prev else prev[i][1])
        curr.append((subx, suby))
        
        if subx == suby and subx > 0:
          count += 1
      
      curr, prev = prev, curr
      curr.clear()
    
    return count
  