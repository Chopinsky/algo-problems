'''
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

Example 1:

Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
Example 2:

Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m * n <= 10^5
matrix[i][j] is either 0 or 1.
'''

from typing import List
from collections import defaultdict


class Solution:
  def largestSubmatrix(self, mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    row = [0]*n
    area = 0
    
    for i in range(m):
      for j in range(n):
        if mat[i][j] == 0:
          row[j] = 0
        else:
          row[j] += 1
        
      col = 0
      for h in sorted(row, reverse=True):
        if h == 0:
          break
          
        col += 1
        area = max(area, col*h)
        
    return area  
        
        
  def largestSubmatrix(self, matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    row = [0] * n
    height = defaultdict(int)
    mx_area = 0
    
    for i in range(m):
      height.clear()
      
      for j in range(n):
        if matrix[i][j] == 0:
          row[j] = 0
        else:
          row[j] += 1
          height[row[j]] += 1
      
      col = 0
      # print(i, height)
      
      for h0 in sorted(height, reverse=True):
        col += height[h0]
        mx_area = max(mx_area, col*h0)
  
    return mx_area
  