'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''


from typing import List


class Solution:
  def spiralOrder(self, mat: List[List[int]]) -> List[int]:
    h, w = len(mat), len(mat[0])
    ans = []
    os = 0
    
    while os <= h-os-1 and os <= w-os-1:
      # print(os)
      if os == h-os-1:
        for j in range(os, w-os):
          ans.append(mat[os][j])
          
        break
        
      if os == w-os-1:
        for i in range(os, h-os):
          ans.append(mat[i][os])
          
        break
        
      for j in range(os, w-os-1):
        ans.append(mat[os][j])
        
      for i in range(os, h-os-1):
        ans.append(mat[i][w-os-1])
        
      if os != h-os-1:
        for j in range(w-os-1, os, -1):
          ans.append(mat[h-os-1][j])
          
      if os != w-os-1:
        for i in range(h-os-1, os, -1):
          ans.append(mat[i][os])
      
      os += 1
      
    # print(os, h-os-1, w-os-1)
    
    return ans