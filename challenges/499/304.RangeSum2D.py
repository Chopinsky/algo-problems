'''
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example 1:

Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-10 ** 5 <= matrix[i][j] <= 10 ** 5
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
'''

from typing import List


class NumMatrix:
  def __init__(self, matrix: List[List[int]]):
    m, n = len(matrix), len(matrix[0])
    self.prefix = [[matrix[i][j] for j in range(n)] for i in range(m)]
    
    for i in range(m):
      row = 0
      for j in range(n):
        row += matrix[i][j]
        self.prefix[i][j] = row + (self.prefix[i-1][j] if i > 0 else 0)
    
    # print(self.prefix)

    
  def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
    a0 = self.prefix[r2][c2]
    a3 = self.prefix[r1-1][c1-1] if r1 > 0 and c1 > 0 else 0
    
    a1 = self.prefix[r1-1][c2] if r1 > 0 else 0
    a2 = self.prefix[r2][c1-1] if c1 > 0 else 0
    
    # print('='*8)
    # print(r1, c1, r2, c2)
    # print(a0, a3, a1, a2)
    
    return a0 + a3 - a1 - a2
  

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


class NumMatrix0:
  def __init__(self, m: List[List[int]]):
    self.presum = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    for i, row in enumerate(m):
      total = 0
      for j, cell in enumerate(row):
        total += cell
        self.presum[i][j] = total if i == 0 else self.presum[i-1][j]+total


  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    top = 0 if row1 == 0 else self.presum[row1-1][col2]
    left = 0 if col1 == 0 else self.presum[row2][col1-1]
    top_left = 0 if (row1 == 0 or col1 == 0) else self.presum[row1-1][col1-1]
    return self.presum[row2][col2] - top - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)