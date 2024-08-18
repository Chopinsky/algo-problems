'''
2373. Largest Local Values in a Matrix

You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

Example 1:

Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
Example 2:

Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.

Constraints:

n == grid.length == grid[i].length
3 <= n <= 100
1 <= grid[i][j] <= 100
'''

from typing import List

class Solution:
  def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    ans = []
    
    def get_val(x: int, y: int) -> int:
      val = grid[x][y]
      
      for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        x1, y1 = x+dx, y+dy
        if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n:
          continue
          
        val = max(val, grid[x1][y1])
      
      return val
    
    for x in range(1, n-1):
      row = []
      for y in range(1, n-1):
        row.append(get_val(x, y))
      
      ans.append(row)
    
    return ans
        