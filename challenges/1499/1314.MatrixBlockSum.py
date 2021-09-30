'''
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100
'''


from typing import List


class Solution:
  def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
    h, w = len(mat), len(mat[0])
    block = [[0]*w for _ in range(h)]
    s = [[0]*w for _ in range(h)]
    
    for i in range(h):
      row = 0
      for j in range(w):
        row += mat[i][j]
        if i > 0:
          block[i][j] += block[i-1][j]  
          
        block[i][j] += row
    
    # for r in block:
    #   print(r)
    
    for i in range(h):
      for j in range(w):
        tl = block[i-k-1][j-k-1] if i-k-1 >= 0 and j-k-1 >= 0 else 0
        top = block[i-k-1][min(j+k, w-1)] if i-k-1 >= 0 else 0
        left = block[min(i+k, h-1)][j-k-1] if j-k-1 >= 0 else 0
        center = block[min(i+k, h-1)][min(j+k, w-1)]
        # print(i, j, tl, top, left, center)
        s[i][j] = center + tl - top - left
    
    return s
  