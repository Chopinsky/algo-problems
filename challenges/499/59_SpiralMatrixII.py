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
    