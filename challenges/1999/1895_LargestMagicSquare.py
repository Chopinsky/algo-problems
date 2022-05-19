'''
A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

Example 1:

Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12
Example 2:

Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 10^6
'''

from typing import List


class Solution:
  def largestMagicSquare(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    preSumRow = [[0] * (n + 1) for _ in range(m)]
    preSumCol = [[0] * (m + 1) for _ in range(n)]
    
    for r in range(m):
      for c in range(n):
        preSumRow[r][c + 1] = preSumRow[r][c] + grid[r][c]
        preSumCol[c][r + 1] = preSumCol[c][r] + grid[r][c]

    def getSumRow(row, l, r):  # row, l, r inclusive
      return preSumRow[row][r + 1] - preSumRow[row][l]

    def getSumCol(col, t, b):  # col, l, r inclusive
      return preSumCol[col][t + 1] - preSumCol[col][b]

    def test(k):
      for r in range(m - k + 1):
        for c in range(n - k + 1):
          d1, d2 = 0, 0
          for d in range(k):
            d1 += grid[r + d][c + d]
            d2 += grid[r + d][c + k - 1 - d]

          match = (d1 == d2)
          nr, nc = r, c

          while nr < r + k and match:
            match = (d1 == getSumRow(nr, c, c + k - 1))
            nr += 1

          while nc < c + k and match:
            match = (d1 == getSumCol(nc, r, r + k - 1))
            nc += 1

          if match:
            return True  # if all the sums is equal then return True as valid

      return False

    for k in range(min(m, n), 1, -1):
      if test(k): 
        return k  # the first valid `k` is the maximum result

    return 1
        