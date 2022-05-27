'''
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Example 1:

Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:

Input: grid = [[0]]
Output: 1

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.
'''

from typing import List


class Solution:
  def matrixScore(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    def flip_row(g, i):
      for j in range(n):
        g[i][j] = 1 - g[i][j]
        
      return g
    
    def flip_col(g, j):
      for i in range(m):
        g[i][j] = 1 - g[i][j]
        
      return g
    
    def count(g):
      total = 0
      
      for i in range(m):
        curr = 0
        for j in range(n):
          curr <<= 1
          if g[i][j] == 1:
            curr |= 1
            
        total += curr
          
      return total
    
    def flip(g: List[List[int]], one: bool) -> int:
      for i in range(m):
        if (one and g[i][0] == 0) or (not one and g[i][0] == 1):
          g = flip_row(g, i)
      
      if not one:
        g = flip_col(g, 0)
        
      for j in range(1, n):
        ones, zeros = 0, 0
        for i in range(m):
          if g[i][j] == 1:
            ones += 1
          else:
            zeros += 1
            
        if ones < zeros:
          g = flip_col(g, j)
          
      return count(g) 
      
    return max(count(grid), 
               flip(grid.copy(), True), 
               flip(grid.copy(), False))
  