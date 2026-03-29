'''
3070. Count Submatrices with Top-Left Element and Sum Less Than k
'''


class Solution:
  def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
    cnt = 0
    m = len(grid)
    n = len(grid[0])
    
    for i in range(m):
      area = 0
      for j in range(n):
        if i > 0:
          grid[i][j] += grid[i-1][j]

        area += grid[i][j]
        if area <= k:
          cnt += 1

    return cnt
        
  def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
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
      