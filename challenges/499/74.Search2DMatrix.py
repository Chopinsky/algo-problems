'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
'''

from typing import List


class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    if target < matrix[0][0] or target > matrix[m-1][n-1]:
      return False
    
    l, r = 0, m*n
    
    while l <= r:
      mid = (l + r) // 2
      x, y = mid//n, mid%n
      val = matrix[x][y]
      # print(x, y)
      
      if val == target:
        return True
      
      if val < target:
        l = mid + 1
      else:
        r = mid - 1
        
    return False
        

  def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
    if not mat:
      return False

    m, n = len(mat), len(mat[0])
    if target < mat[0][0] or target > mat[m-1][n-1]:
      return False
    
    l, r = 0, m*n
    
    while l < r:
      mid = (l + r) // 2
      mv = mat[mid//n][mid%n]
      
      # print('left', l//n, l%n, 'right', r//n, r%n)
      # print(mid//n, mid%n, mv)
      
      if mv == target:
        return True
      
      if mv < target:
        l = mid + 1
      else:
        r = mid - 1
        
    # print(l, r)
    if 0 <= r < m*n and mat[r//n][r%n] == target:
      return True
    
    return False
  