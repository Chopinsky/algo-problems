'''
1277. Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''

from typing import List


class Solution:
  def countSquares(self, mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    prefix = [[val for val in row] for row in mat]
    count = 0

    for x in range(m):
      row = 0
      for y in range(n):
        row += mat[x][y]
        prefix[x][y] = row + (prefix[x-1][y] if x > 0 else 0)

    # print('init:', prefix)
    def is_one_square(x0: int, y0: int, x1: int, y1: int) -> bool:
      if x0 == x1 and y0 == y1:
        return mat[x0][y0] == 1

      tl = prefix[x0-1][y0-1] if x0 > 0 and y0 > 0 else 0
      top = prefix[x0-1][y1] if x0 > 0 else 0
      left = prefix[x1][y0-1] if y0 > 0 else 0
      br = prefix[x1][y1]
      
      expected = (x1-x0+1) * (y1-y0+1)
      curr = br - top - left + tl
      # print('count:', (x0, y0), (x1, y1), expected, curr, tl, top, left, br)

      return expected == curr

    for x in range(m):
      for y in range(n):
        if mat[x][y] == 0:
          continue

        for k in range(min(x, y)+1):
          if not is_one_square(x-k, y-k, x, y):
            break

          count += 1
          # print('square:', (x-k, y-k), (x, y))

    return count
        
  def countSquares(self, matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    prefix = [[0]*n for _ in range(m)]
    total = 0
    
    def count_ones(x: int, y: int, side: int) -> int:
      if not matrix[x][y] or side > x+1 or side > y+1:
        return 0
      
      if side == 1:
        return 1
      
      if x+1 == side and y+1 == side:
        return prefix[x][y]
      
      if x+1 == side:
        return prefix[x][y] - prefix[x][y-side]
      
      if y+1 == side:
        return prefix[x][y] - prefix[x-side][y]
        
      return prefix[x][y] - prefix[x-side][y] - prefix[x][y-side] + prefix[x-side][y-side]
    
    for i in range(m):
      row = 0
      for j in range(n):
        row += matrix[i][j]
        if i == 0:
          prefix[i][j] = row
        else:
          prefix[i][j] = row + prefix[i-1][j]
          
        side = 1
        while side <= 1+min(i, j):
          cnt = count_ones(i, j, side)
          # print(i, j, side, cnt)
          if cnt < side * side:
            break
            
          total += 1
          side += 1
          
    # print(prefix)
    return total
    