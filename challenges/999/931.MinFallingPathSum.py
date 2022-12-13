'''
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum underlined below:
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]

Example 2:

Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is underlined below:
[[-19,57],
 [-40,-5]]
Example 3:

Input: matrix = [[-48]]
Output: -48

Constraints:

n == matrix.length
n == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
'''

from typing import List


class Solution:
  def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    curr, nxt = [val for val in matrix[0]], []
    h, w = len(matrix), len(matrix[0])
    
    for r in range(1, h):
      for c in range(w):
        val = curr[c]
        
        if c > 0:
          val = min(val, curr[c-1])
          
        if c < w-1:
          val = min(val, curr[c+1])
        
        nxt.append(val + matrix[r][c])
        
      curr, nxt = nxt, curr
      nxt.clear()
    
    return min(curr)
    

  def minFallingPathSum(self, mat: List[List[int]]) -> int:
    h, w = len(mat), len(mat[0])
    dp = [[mat[i][j] if i == 0 else float('inf') for j in range(w)] for i in range(h)]
    
    for i in range(1, h):
      for j in range(w):
        dp[i][j] = mat[i][j] + dp[i-1][j]
        
        if j > 0:
          dp[i][j] = min(dp[i][j], mat[i][j] + dp[i-1][j-1])
          
        if j < w-1:
          dp[i][j] = min(dp[i][j], mat[i][j] + dp[i-1][j+1])
    
    return min(dp[-1])