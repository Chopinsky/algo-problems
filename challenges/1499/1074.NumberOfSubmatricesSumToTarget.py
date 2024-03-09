'''
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:

Input: matrix = [[904]], target = 0
Output: 0

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
'''

from collections import defaultdict
from typing import List

class Solution:
  def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
    seg_sums = {}
    m, n = len(mat), len(mat[0])
    count = 0
    
    for i in range(m):
      for j0 in range(n):
        row = 0
        for j1 in range(j0, -1, -1):
          row += mat[i][j1]
          if (j1, j0) not in seg_sums:
            seg_sums[j1, j0] = { '$': 0 }
            
          if i == 0 and row == target:
            # print('row:', i, (j1, j0))
            count += 1
            
          prefix = row + seg_sums[j1, j0]['$']
          if i > 0 and prefix == target:
            # print('col:', i, (j1, j0))
            count += 1
          
          val = prefix - target
          count += seg_sums[j1, j0].get(val, 0)
          # print(i, (j1, j0), row, prefix, val, seg_sums[j1, j0])
          
          seg_sums[j1, j0][prefix] = 1 + seg_sums[j1, j0].get(prefix, 0)
          seg_sums[j1, j0]['$'] = prefix
          
    return count
  
  
  def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    m, n = len(matrix), len(matrix[0])
    row_sums = [[0]*n for _ in range(m)]
    count = 0
    
    for i in range(m):
      for j in range(n):
        row_sums[i][j] = matrix[i][j] + (0 if j == 0 else row_sums[i][j-1])
    
    for l in range(n):
      for r in range(l, n):
        col_sums = defaultdict(int)
        curr = 0
        
        for i in range(m):
          curr += row_sums[i][r] - (row_sums[i][l-1] if l > 0 else 0)
          if curr == target:
            count += 1
          
          if curr-target in col_sums:
            count += col_sums[curr-target]
          
          col_sums[curr] += 1
    
    return count
    

  # Time complexity: O(MN^2)
  # 1) calculate prefix sum for each row
  # 2) then from col-i to col-j where j >= i, we calculate sum
  #    of sub-matrix (0, i, k, j) from (0, i, k-1, j) and prefix sum
  #    for row-k
  # 3) then the count of sub-matrix added to target equals the number
  #    of previously calculated sub-matrix that added to `currSum - target`
  # 4) add the currSum to the dict so we can keep track of the sums
  def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
    h, w = len(mat), len(mat[0])

    # calc each row's prefix sum for columns
    for i in range(h):
      for j in range(1, w):
        mat[i][j] += mat[i][j-1]

    ans = 0

    # for each column window [i, j] where j >= i, calculate matrix sum
    # for (0, i, k, j) where k is in [0, w); then we can know how many
    # submatrix exists for (k'+1, i, k, j) by looking at how many of the
    # (0, i, k', j) sums to `currSum - target`
    for i in range(w):
      for j in range(i, w):
        # dict to store prefix sums of the sub-matrix
        sumDict = defaultdict(int)
        sumDict[0] = 1   # submatrix itself == 1 count
        currSum = 0

        for k in range(h):
          # get the current sub-matrix's total sum by adding the sum of the
          # cells in this row and between column [i, j]
          currSum += mat[k][j] - (mat[k][i-1] if i > 0 else 0)
          # get the number of the existing sub-matrix sums to the desired value
          ans += sumDict[currSum - target]
          # update the sub-marix sum's dict
          sumDict[currSum] += 1

    return ans
