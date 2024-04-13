'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0
 

Constraints:

rows == matrix.length
cols == matrix[i].length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
'''

from typing import List

class Solution:
  def maximalRectangle(self, mat: List[List[str]]) -> int:
    m, n = len(mat), len(mat[0])
    prefix = [[int(val) for val in mat[i]] for i in range(m)]
    area = 0
    
    for x in range(m):
      for y in range(1, n):
        if mat[x][y] == '0':
          continue
          
        prefix[x][y] += prefix[x][y-1]
        
      # print(prefix[x])
      
    for x0 in range(m):
      for y in range(n):
        if prefix[x0][y] == 0:
          continue
          
        if (x0+1)*(y+1) <= area:
          continue
          
        width = prefix[x0][y]
        area = max(area, width)
        
        for x1 in range(x0, -1, -1):
          if prefix[x1][y] == 0:
            break
            
          width = min(width, prefix[x1][y])
          area = max(area, (x0-x1+1)*width)
          
    return area
        
  def maximalRectangle(self, matrix: List[List[int]]) -> int:
    if not matrix:
      return 0
    
    m, n = len(matrix), len(matrix[0])
    stack = []
    area = 0
    
    for i in range(m):
      stack.clear()
      for j in range(n):
        if matrix[i][j] == '0':
          matrix[i][j] = 0
          stack.clear()
          continue
          
        matrix[i][j] = (matrix[i-1][j] if i > 0 else 0) + 1
        if not stack:
          area = max(area, matrix[i][j])
          stack.append((j, matrix[i][j]))
          continue
          
        last = j
        while stack and stack[-1][1] >= matrix[i][j]:
          idx, _ = stack.pop()
          last = idx
          
        stack.append((last, matrix[i][j]))
        # print(i, j, matrix[i][j], stack, last)
        
        for k, h in stack:
          area = max(area, (j-k+1) * h)
    
    # print('out', matrix)
    return area
        