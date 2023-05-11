'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
'''

from typing import List


class Solution:
  def generateMatrix(self, n: int) -> List[List[int]]:
    mat = [[0]*n for _ in range(n)]
    seen = set()
    x, y = 0, 0
    idx = 0
    dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for i in range(1, n*n+1):
      seen.add((x, y))
      mat[x][y] = i
      x0, y0 = x+dr[idx][0], y+dr[idx][1]
      
      if x0 < 0 or x0 >= n or y0 < 0 or y0 >= n or (x0, y0) in seen:
        idx = (idx + 1) % 4
        x0, y0 = x+dr[idx][0], y+dr[idx][1]
      
      x, y = x0, y0
    
    return mat
    
    
  def generateMatrix(self, n: int) -> List[List[int]]:
    g = [[0 for _ in range(n)] for _ in range(n)]
    val = 1
    i, j = 0, 0
    
    for ln in range(n-1, -1, -2):
      if ln == 0:
        g[i][j] = val
        break
        
      for _ in range(ln):
        g[i][j] = val
        val += 1
        j += 1
        
      for _ in range(ln):
        g[i][j] = val
        val += 1
        i += 1
        
      for _ in range(ln):
        g[i][j] = val
        val += 1
        j -= 1
        
      for _ in range(ln):
        g[i][j] = val
        val += 1
        i -= 1
        
      i += 1
      j += 1
      
    return g
    