'''
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9
'''

from typing import List
from bisect import bisect_left, bisect_right


class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
      if target > matrix[i][-1]:
        continue
        
      if target < matrix[i][0]:
        break
        
      j = bisect_left(matrix[i], target)
      if j < n and matrix[i][j] == target:
        return True
      
    return False

    
  def searchMatrix(self, mat: List[List[int]], t: int) -> bool:
    if t < mat[0][0] or t > mat[-1][-1]:
      return False
    
    h, w = len(mat), len(mat[0])
    rs = bisect_left([mat[i][w-1] for i in range(h)], t)
    re = bisect_right([mat[i][0] for i in range(h)], t)
    
    for r in range(min(rs, h), max(re, h)):
      c = bisect_left(mat[r], t)
      if c < w and mat[r][c] == t:
        return True
      
    return False
    
    
