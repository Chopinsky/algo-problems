'''
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

 

Example 1:

Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation:
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]

Example 2:

Input: rowSum = [5,7,10], colSum = [8,6,8]
Output: [[0,5,0],
         [6,1,0],
         [2,0,8]]

Example 3:

Input: rowSum = [14,9], colSum = [6,9,8]
Output: [[0,9,5],
         [6,0,3]]

Example 4:

Input: rowSum = [1,0], colSum = [1]
Output: [[1],
         [0]]

Example 5:

Input: rowSum = [0], colSum = [0]
Output: [[0]]

Constraints:

1 <= rowSum.length, colSum.length <= 500
0 <= rowSum[i], colSum[i] <= 10^8
sum(rows) == sum(columns)
'''


from typing import List


class Solution:
  def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    row = [[val, i] for i, val in enumerate(rowSum)]    
    row.sort()

    col = [[val, i] for i, val in enumerate(colSum)]
    col.sort()
    
    i, j = 0, 0
    m, n = len(row), len(col)
    grid = [[0]*n for _ in range(m)]
    # print('init', row, col)
    
    while row[m-1][0] and col[n-1][0]:
      # print(i, j, row[i], col[j])
      if not row[i][0] and i < m-1:
        i += 1
        
      if not col[j][0] and j < n-1:
        j += 1
        
      r, c = row[i][1], col[j][1]
      grid[r][c] = min(row[i][0], col[j][0])
      
      row[i][0] -= grid[r][c]
      col[j][0] -= grid[r][c]
        
    return grid
  