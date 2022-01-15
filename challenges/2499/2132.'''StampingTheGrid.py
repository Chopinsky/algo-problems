'''
You are given an m x n binary matrix grid where each cell is either 0 (empty) or 1 (occupied).

You are then given stamps of size stampHeight x stampWidth. We want to fit the stamps such that they follow the given restrictions and requirements:

Cover all the empty cells.
Do not cover any of the occupied cells.
We can put as many stamps as we want.
Stamps can overlap with each other.
Stamps are not allowed to be rotated.
Stamps must stay completely inside the grid.
Return true if it is possible to fit the stamps while following the given restrictions and requirements. Otherwise, return false.

Example 1:

Input: grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3
Output: true
Explanation: We have two overlapping stamps (labeled 1 and 2 in the image) that are able to cover all the empty cells.
Example 2:


Input: grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2 
Output: false 
Explanation: There is no way to fit the stamps onto all the empty cells without the stamps going outside the grid.

Constraints:

m == grid.length
n == grid[r].length
1 <= m, n <= 10^5
1 <= m * n <= 2 * 10^5
grid[r][c] is either 0 or 1.
1 <= stampHeight, stampWidth <= 10^5
'''


from typing import List


class Solution:
  '''
  the idea is to loop over all rows first, and update how many 0s are before the current
  cell, as long as there are more than `w` 0s between 1s in each row, the row check will pass;
  then we will try stamp the grid from the bottom-right cornern: we check how many rows that 
  have `w` or more columns of 0s, and see if the number of such rows is equal or greater than
  `h` -- if so, we can stamp the bottom-right corner and cover all these rows, otherwise, we
  don't have enough rows of 0s to be stamped, or we will stamp on 1s.
  '''
  def possibleToStamp(self, grid: List[List[int]], h: int, w: int) -> bool:
    m, n = len(grid), len(grid[0])
    consec = grid.copy()
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          # if 1 appears too soon, 0s before it has less 
          # conseutive columns, they won't be stamped
          if j > 0 and 0 < consec[i][j-1] < w:
            return False
          
          # consecutive counter reset to 0
          consec[i][j] = 0
          
        elif j == 0:
          # consecutive counter init condition
          consec[i][j] = 1
          
        else:
          # increament the consecutive counter
          consec[i][j] = consec[i][j-1] + 1

      # last few 0s don't have enough columns to be stamped
      if 0 < consec[i][n-1] < w:
        return False

    for j in range(n):
      # number of rows that will have at least `w` width
      # before and including the current row
      cnt = 0
      
      for i in range(m):
        if consec[i][j] < w:
          # there are rows before i-th row that have at 
          # least `w` width, but we don't have `h` height
          # for them to be stamped, not gonna make it
          if 0 < cnt < h:
            return False
          
          # all previous cells can be stamped, reset
          cnt = 0
          
        else:
          # we have `cnt` rows above here that have at least
          # w width, and hence can be stamped from the top
          # left corner if cnt >= h
          cnt += 1

      # not enough space for the last few rows of
      # the 0s to be stamped, as we don't have enough
      # rows with at least `w` width columns left 
      if 0 < cnt < h:
        return False

    return True
      