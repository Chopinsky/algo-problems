'''
3070. Count Submatrices with Top-Left Element and Sum Less Than k
'''

class Solution:
  def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
    count = 0
    if grid[0][0] > k:
      return count
    
    m, n = len(grid), len(grid[0])
    prev, row = [0]*n, []
    prefix = 0
    
    for x in range(m):
      for y in range(n):
        val = grid[x][y]
        prefix += val
        top = prev[y]
        
        row.append(prefix + top)
        if row[-1] <= k:
          count += 1

      # print(row)
      prev, row = row, prev
      row.clear()
      prefix = 0

    return count
      