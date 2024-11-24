'''
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

Example 1:

Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.

Example 2:

Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.

Constraints:

n == matrix.length == matrix[i].length
2 <= n <= 250
-10^5 <= matrix[i][j] <= 10^5
'''

from typing import List


class Solution:
  def maxMatrixSum(self, matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    s0 = 0
    has_zero = False
    neg_count = 0
    low = abs(matrix[0][0])
    
    for x in range(m):
      for y in range(n):
        val = matrix[x][y]
        if val == 0:
          has_zero = True
          continue
          
        s0 += abs(val)
        low = min(low, abs(val))
        
        if val < 0:
          neg_count += 1
        
    if has_zero or (neg_count % 2 == 0):
      return s0
    
    return s0 - 2*low
      
  '''
  the trick is to understand that you can roll the operations, such that any 2 numbers 
  in the matrix can form a "pair" and flip the signs; as a result, if we have even number
  of negative numbers, all of them can form a "pair" and all flip to positive numbers; otherwise,
  we will be left with a single negative number, and we can pair it with the smallest absolute
  value in the matrix and flip this pair, ending with the smallest absolute value to be negative,
  therefore maximizing the total sum.
  '''
  def maxMatrixSum(self, matrix: List[List[int]]) -> int:
    sums, low, rows = 0, abs(matrix[0][0]), 0
    for i in range(len(matrix)):
      neg_count = 0
      for val in matrix[i]:
        if val < 0:
          neg_count += 1
          
        sums += abs(val)
        low = min(low, abs(val))
        
      if neg_count%2 == 1:
        rows += 1
        
    # print(rows)
    if rows % 2 == 1:
      sums -= 2*low
    
    return sums
