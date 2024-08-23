from typing import List

class Solution:
  def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix), len(matrix[0])
    row_min = [float('inf')]*m
    col_max = [0]*n
    
    for r in range(m):
      for c in range(n):
        val = matrix[r][c]
        row_min[r] = min(row_min[r], val)
        col_max[c] = max(col_max[c], val)
      
    lucky_vals = []
    # print(row_min, col_max)
    
    for r in range(m):
      for c in range(n):
        val = matrix[r][c]
        if val == row_min[r] and val == col_max[c]:
          lucky_vals.append(val)
    
    return lucky_vals
        