'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


from typing import List


class Solution:
  def setZeroes(self, mat: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    h, w = len(mat), len(mat[0])
    r = [False] * h
    c = [False] * w
    
    for i in range(h):
      for j in range(w):
        if mat[i][j] == 0:
          r[i] = True
          c[j] = True
          
    for i, zero in enumerate(r):
      if not zero:
        continue
        
      for j in range(w):
        mat[i][j] = 0
        
    for j, zero in enumerate(c):
      if not zero:
        continue
        
      for i in range(h):
        mat[i][j] = 0
        