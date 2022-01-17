'''
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.

Example 1:

Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
Output: 5
Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
Example 2:

Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
Output: 0
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
grid[i][j] is -1, 0, or 1.
grid[0][0] != -1
grid[n - 1][n - 1] != -1
'''


from typing import List
from functools import lru_cache


class Solution:
  '''
  the idea is to think of the process as 2 ppl picking up cherries, both
  start at (0, 0) and end at (n-1, n-1)
  '''
  def cherryPickup(self, grid: List[List[int]]) -> int:
    n = len(grid)
    
    @lru_cache(None)
    def dp(x0: int, y0: int, x1: int) -> int:
      y1 = x0 + y0 - x1
      
      # invalid case
      if x0 >= n or y0 >= n or x1 >= n or y1 >= n or grid[x0][y0] == -1 or grid[x1][y1] == -1:
        return -1
      
      # both ppl reached the destination
      if x0 == n-1 and y0 == n-1:
        return grid[x0][y0]
      
      # get the cherry from cell (x0, y0)
      count = grid[x0][y0]
      
      # if the 2nd ppl is not at the same cell, add cherry
      # from (x1, y1) as well
      if x0 != x1 and y0 != y1:
        count += grid[x1][y1]
        
      nxt_pickup = -1
      
      # both moves right
      rr = dp(x0, y0+1, x1)
      if rr >= 0:
        nxt_pickup = max(nxt_pickup, rr)
        
      # 1 moves right, 2 moves down
      rd = dp(x0, y0+1, x1+1)
      if rd >= 0:
        nxt_pickup = max(nxt_pickup, rd)
        
      # 1 moves down, 2 moves right
      dr = dp(x0+1, y0, x1)
      if dr >= 0:
        nxt_pickup = max(nxt_pickup, dr)

      # 1 moves down, 2 moves down
      dd = dp(x0+1, y0, x1+1)
      if dd >= 0:
        nxt_pickup = max(nxt_pickup, dd)
      
      return count + nxt_pickup if nxt_pickup >= 0 else -1
      
    return max(0, dp(0, 0, 0))
  