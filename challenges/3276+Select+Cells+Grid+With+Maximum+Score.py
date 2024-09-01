'''
3276. Select Cells in Grid With Maximum Score

You are given a 2D matrix grid consisting of positive integers.

You have to select one or more cells from the matrix such that the following conditions are satisfied:

No two selected cells are in the same row of the matrix.
The values in the set of selected cells are unique.
Your score will be the sum of the values of the selected cells.

Return the maximum score you can achieve.

Example 1:

Input: grid = [[1,2,3],[4,3,2],[1,1,1]]

Output: 8

Explanation:

We can select the cells with values 1, 3, and 4 that are colored above.

Example 2:

Input: grid = [[8,7,6],[8,3,2]]

Output: 15

Explanation:

We can select the cells with values 7 and 8 that are colored above.

Constraints:

1 <= grid.length, grid[i].length <= 10
1 <= grid[i][j] <= 100
'''

from typing import List
from functools import lru_cache

class Solution:
  def maxScore(self, grid: List[List[int]]) -> int:
    cand = []
    m, n = len(grid), len(grid[0])
    
    for x in range(m):
      for y in range(n):
        cand.append((grid[x][y], x))
        
    cand.sort(reverse=True)
    jumps = {}
    prev = -1
    ln = len(cand)
    
    for i in range(ln):
      val, _ = cand[i]
      if prev > 0 and prev != val:
        jumps[prev] = i
        
      prev = val
    
    jumps[prev] = ln
    # print('init:', cand, jumps)
    
    @lru_cache(None)
    def dp(i: int, mask: int) -> int:
      if i >= ln:
        return 0
      
      # if skip this number
      total = dp(i+1, mask)
      val, row = cand[i]
      
      # this row is already used, done
      if (1<<row) & mask > 0:
        return total
      
      # if take this number
      mask |= (1 << row)
      j = jumps[val]
      total = max(total, val+dp(j, mask))
      # print('dp:', (i, bin(mask)[2:]), total)
      
      return total
    
    return dp(0, 0)
    