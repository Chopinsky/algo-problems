'''

'''

from typing import List


class Solution:
  def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
    m, n = len(mat), len(mat[0])
    l, r = 0, n
    
    def search(j: int):
      max_val = -1
      row = -1
      lval, rval = -1, -1
      
      for i in range(m):
        if mat[i][j] > max_val:
          max_val = mat[i][j]
          row = i
          lval = mat[i][j-1] if j > 0 else -1
          rval = mat[i][j+1] if j < n-1 else -1
          
      if max_val > lval and max_val > rval:
        return True, row
      
      return False, -1 if max_val < lval else 1
    
    while l <= r:
      col = (l + r) // 2
      # print(col, l, r)
      
      found, data = search(col)
      if found:
        return [data, col]
      
      if data < 0:
        r = col-1
      else:
        l = col+1
    
    return [-1, -1]

    
  def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
    m, n = len(mat), len(mat[0])
    
    for i in range(m):
      for j in range(n):
        cnt = 0
        if i == 0 or mat[i][j] > mat[i-1][j]:
          cnt += 1
          
        if i == m-1 or mat[i][j] > mat[i+1][j]:
          cnt += 1
          
        if j == 0 or mat[i][j] > mat[i][j-1]:
          cnt += 1
          
        if j == n-1 or mat[i][j] > mat[i][j+1]:
          cnt += 1
          
        if cnt == 4:
          return [i, j]
          
    return [-1, -1]
        