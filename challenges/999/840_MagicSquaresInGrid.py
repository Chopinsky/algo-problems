'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:

Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
'''

from typing import List


class Solution:
  def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    if m < 3 or n < 3:
      return 0
    
    def check_rows(i, j):
      r0 = sum(grid[i][j:j+3])
      r1 = sum(grid[i+1][j:j+3])
      r2 = sum(grid[i+2][j:j+3])
      
      if r0 == r1 == r2:
        return r0
      
      return -1
    
    def check_cols(i, j):
      c0 = sum(grid[r][j] for r in range(i, i+3))
      c1 = sum(grid[r][j+1] for r in range(i, i+3))
      c2 = sum(grid[r][j+2] for r in range(i, i+3))
      
      if c0 == c1 == c2:
        return c0
      
      return -1
    
    def check_diag(i, j):
      d1 = sum(grid[i+o][j+o] for o in range(3))
      d2 = sum(grid[i+o][j+2-o] for o in range(3))
      
      if d1 == d2:
        return d1
      
      return -1
    
    def check_uniq(i, j):
      nums = set()
      for o in range(3):
        nums |= set(grid[i+o][j:j+3])
        
      return len([val for val in nums if 1 <= val <= 9]) == 9
    
    count = 0
    for i in range(m-2):
      for j in range(n-2):
        if not check_uniq(i, j):
          continue
          
        r = check_rows(i, j) 
        if r < 0:
          continue
          
        c = check_cols(i, j)
        if c < 0 or r != c:
          continue
        
        if r != c:
          continue
          
        if check_diag(i, j) == r:
          print(r, c, check_diag(i, j))
          count += 1
          
    return count
  