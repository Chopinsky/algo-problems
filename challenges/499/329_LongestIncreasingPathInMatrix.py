'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
'''

from typing import List
from functools import lru_cache


class Solution:
  def longestIncreasingPath(self, mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    long = 1

    inc = [[1]*n for _ in range(m)]
    stack = [(mat[i][j], i, j) for j in range(n) for i in range(m)]
    stack.sort(reverse=True)
    
    for val, x, y in stack:
      # print('check:', val, x, y)
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or val >= mat[x0][y0]:
          continue
          
        inc[x][y] = max(inc[x][y], 1+inc[x0][y0])
      
      long = max(long, inc[x][y])
    
    # print(inc)
    return long
  
  
  def longestIncreasingPath0(self, mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    # inc = [[0]*n for _ in range(m)]
    long = 1
    
    @lru_cache(None)
    def move(x: int, y: int):
      sl = 1
      val = mat[x][y]
      
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
          continue

        if mat[x0][y0] <= val:
          continue

        sl = max(sl, 1+move(x0, y0))
        
      return sl
    
    for i in range(m):
      for j in range(n):
        long = max(long, move(i, j))
        
    return long
    