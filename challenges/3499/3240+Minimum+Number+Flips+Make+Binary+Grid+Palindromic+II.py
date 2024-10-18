'''
3240. Minimum Number of Flips to Make Binary Grid Palindromic II
'''

from typing import List


class Solution:
  def minFlips(self, A: List[List[int]]) -> int:
    res = 0
    one = 0
    diff = 0
    m, n = len(A), len(A[0])

    for i in range(m//2):
      for j in range(n//2):
        v = A[i][j] + A[i][~j] + A[~i][j] + A[~i][~j]
        res += min(v, 4-v)
        
    if n % 2:
      for i in range(m//2):
        diff += A[i][n//2] ^ A[~i][n//2]
        one += A[i][n//2] + A[~i][n//2]
        
    if m % 2:
      for j in range(n//2):
        diff += A[m//2][j] ^ A[m//2][~j]
        one += A[m//2][j] + A[m//2][~j]
        
    if n % 2 and m % 2:
      res += A[m//2][n//2]
      
    if diff == 0 and one % 4:
      res += 2
      
    return res + diff
      