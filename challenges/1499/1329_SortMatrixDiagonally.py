'''
1329. Sort the Matrix Diagonally

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
Example 2:

Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
'''

from typing import List


class Solution:
  def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    vals = []
    
    for diag in range(n-2, 1-m, -1):
      vals.clear()
      
      if diag >= 0:
        x0, y0 = 0, diag
      else:
        x0, y0 = -diag, 0
      
      x, y = x0, y0
      while x < m and y < n:
        vals.append(mat[x][y])
        x += 1
        y += 1
        
      vals.sort()
      idx = 0
      
      while x0 < m and y0 < n:
        mat[x0][y0] = vals[idx]
        x0 += 1
        y0 += 1
        idx += 1
        
    return mat
        