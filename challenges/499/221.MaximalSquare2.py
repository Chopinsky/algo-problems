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
  def maximalSquare(self, matrix: List[List[str]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0]*cols for _ in range(rows)]
    max_side = 0
    
    # Initialize boundary row
    for row in range(rows):
      if matrix[row][0] == "1":
        dp[row][0] = 1
        max_side = 1
          
      if matrix[row][cols-1] == "1":
        dp[row][cols-1] = 1
        max_side = 1

    # Initialize boundary col
    for col in range(cols):
      if matrix[0][col] == "1":
        dp[0][col] = 1
        max_side = 1
          
      if matrix[rows-1][col] == "1":
        dp[rows-1][col] = 1
        max_side = 1

    for row in range(1, rows):
      for col in range(1, cols):
        if matrix[row][col] != "1":
          continue
          
        dp[row][col] = 1 + min(
          dp[row-1][col], 
          dp[row-1][col-1], 
          dp[row][col-1]
        )

        if dp[row][col] > max_side:
          max_side = dp[row][col]

    return max_side * max_side
  