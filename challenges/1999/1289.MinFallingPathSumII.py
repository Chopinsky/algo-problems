'''
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

Example 1:

Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.

Example 2:

Input: grid = [[7]]
Output: 7
 
Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
'''


from typing import List


class Solution:
  def minFallingPathSum(self, grid: List[List[int]]) -> int:
    h = len(grid)
    if h == 1:
      return grid[0][0]
    
    m0, m1 = (0, -1), (0, -1)
    for r in grid:
      n0, n1 = None, None
      
      for i, v in enumerate(r):
        v = v + (m0[0] if i != m0[1] else m1[0])
        
        if not n0:
          n0 = (v, i)
          continue

        if not n1:
          n1 = (v, i)
          if n0[0] > n1[0]:
            n0, n1 = n1, n0
            
          continue

        if v <= n0[0]:
          n1 = n0
          n0 = (v, i)
          continue

        if v < n1[0]:
          n1 = (v, i)
    
      # print(n0, n1)
      m0, m1 = n0, n1
      
    return m0[0]
  