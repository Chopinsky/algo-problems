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
    
    def check(x: int, y: int) -> bool:
      if x+2 >= m or y+2 >= n:
        return False
      
      s = set(i for i in range(1, 10))
      rows = [0]*3
      cols = [0]*3
      d0 = 0
      d1 = 0
      
      for x0 in range(x, x+3):
        # print('cr:', grid[x0][y:y+3])
        for y0 in range(y, y+3):
          val = grid[x0][y0]
          if val not in s:
            return False
          
          s.discard(val)
          dx = x0-x
          dy = y0-y
          
          rows[dx] += val
          cols[dy] += val
          
          if dx == dy:
            d0 += val
            
          if dx == 2-dy:
            d1 += val
      
      # print('check:', (x, y), rows, cols, d0, d1)
      if len(s) > 0 or d0 != d1:
        return False
      
      return all(v == d0 for v in rows+cols)
    
    count = 0
    for x in range(m-2):
      for y in range(n-2):
        if check(x, y):
          count += 1
    
    return count
        
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
  