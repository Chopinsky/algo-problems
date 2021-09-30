'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:

Input: matrix = [["0"]]
Output: 0

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
'''


from typing import List


class Solution:
  def maximalSquare(self, m: List[List[str]]) -> int:
    if not m:
      return 0
    
    h, w = len(m), len(m[0])
    row = [1 if m[0][j] == '1' else 0 for j in range(w)]
    max_size = max(row)
    
    for r in m[1:]:
      nxt = [0] * w
      nxt[0] = 1 if r[0] == '1' else 0
      max_size = max(max_size, nxt[0])
      
      for j in range(1, w):
        if r[j] == '0':
          continue
          
        nxt[j] = min(nxt[j-1], row[j], row[j-1]) + 1
        max_size = max(max_size, nxt[j])
        
      row = nxt
      
    return max_size * max_size
    
    
  def maximalSquare0(self, m: List[List[str]]) -> int:
    h, w = len(m), len(m[0])
    dp = [[1 if i == 0 and m[i][j] == '1' else 0 for j in range(w)] for i in range(h)]
    max_size = 1 if any(dp[0][j] == 1 for j in range(w)) else 0
    
    for i in range(1, h):
      for j in range(w):
        if m[i][j] == '0':
          continue
          
        dp[i][j] = dp[i-1][j] + 1
        k = 1
        low = dp[i][j]
        
        while k <= j and k <= low-1 and dp[i][j-k] >= k+1:
          low = min(low, dp[i][j-k])
          k += 1
        
        # print(i, j, k)
        k = min(k, low)
        max_size = max(max_size, k*k)
        
    # print(dp)
    
    return max_size
    
    