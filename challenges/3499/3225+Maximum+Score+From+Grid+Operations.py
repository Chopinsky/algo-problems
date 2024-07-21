'''
3225. Maximum Score From Grid Operations

You are given a 2D matrix grid of size n x n. Initially, all cells of the grid are colored white. In one operation, you can select any cell of indices (i, j), and color black all the cells of the jth column starting from the top row down to the ith row.

The grid score is the sum of all grid[i][j] such that cell (i, j) is white and it has a horizontally adjacent black cell.

Return the maximum score that can be achieved after some number of operations.

Example 1:

Input: grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]

Output: 11

Explanation:

In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is grid[3][0] + grid[1][2] + grid[3][3] which is equal to 11.

Example 2:

Input: grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]

Output: 94

Explanation:

We perform operations on 1, 2, and 3 down to rows 1, 4, and 0, respectively. The score of the resulting grid is grid[0][0] + grid[1][0] + grid[2][1] + grid[4][1] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] + grid[0][4] which is equal to 94.

Constraints:

1 <= n == grid.length <= 100
n == grid[i].length
0 <= grid[i][j] <= 10^9

Test cases:

[[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]
[[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]
[[0,1,9,9,8],[0,0,4,0,1],[6,7,0,6,0],[1,1,0,14,0],[14,0,15,13,13]]
'''

from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
  def maximumScore(self, grid: List[List[int]]) -> int:
    n = len(grid)
    if n == 1:
      return 0
    
    if n == 2:
      return max(
        sum(grid[i][0] for i in range(n)),
        sum(grid[i][1] for i in range(n)),
      )

    real = defaultdict(int)
    full = defaultdict(int)
    bar = defaultdict(int)

    def init():
      vals = {}
      for i in range(-1, n):
        for j in range(-1, n):
          if i == j:
            vals[i, j] = 0
            continue
            
          if i > j:
            vals[i, j] = vals[i-1, j] + grid[i][1]
          else:
            vals[i, j] = vals[i, j-1] + grid[j][0]
    
      curr = defaultdict(int)
      for (i, j), val in vals.items():
        if i <= j:
          curr[j, 0] = max(curr[j, 0], vals[i, j])
        else:
          curr[j, i-j] = max(curr[j, i-j], vals[i, j])
      
      # print('init-1:', curr)
      return curr
    
    def update(curr, nxt, c):
      prefix = [0]
      for r in range(n):
        prefix.append(prefix[-1] + grid[r][c])
        
      real.clear()
      full.clear()
      bar.clear()
      
      # O(n^2*log(n)) ~ 5*10^4
      for k, val in curr.items():
        i, j = k
        
        # hybrid mode updates
        real[i+j] = max(real[i+j], val)
        real[i] = max(real[i], val)
        bar[i] = max(bar[i], val)

        if j == 0:
          full[i] = max(full[i], val)
      
      # update the real parts first
      prev_full = curr[-1, 0]
      
      for i in range(-1, n):
        if i == -1:
          nxt[i, 0] = max(curr[-1, i] for i in range(0, n+1))
          continue
          
        prev_full += grid[i][c-1]
        
        nxt[i, 0] = max(
          # bars at diff heights, unlock the cell @ (i, c-1)
          prev_full, 
          # bars at the same height
          real[i],
        )
        
        prev_full = max(prev_full, full[i])
        # print('update-0:', i, nxt[i, 0], (real[i], full[i], grid[i][c-1], prev_full))
      
      # update the imagine parts next
      for i in range(-1, n):
        for j in range(1, n+1):
          if i+j >= n:
            break
          
          nxt[i, j] = bar[i+j] + (prefix[i+j+1]-prefix[i+1])

      # print('update-1:', nxt)
      
      return nxt, curr
    
    curr = init()
    nxt = defaultdict(int)
    
    for c in range(2, n):
      curr, nxt = update(curr, nxt, c)
      nxt.clear()
    
    return 0 if not curr else max(curr.values())
    
        