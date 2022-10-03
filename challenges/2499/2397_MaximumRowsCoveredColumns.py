'''
2397. Maximum Rows Covered by Columns

You are given a 0-indexed m x n binary matrix mat and an integer cols, which denotes the number of columns you must choose.

A row is covered by a set of columns if each cell in the row that has a value of 1 also lies in one of the columns of the chosen set.

Return the maximum number of rows that can be covered by a set of cols columns.

Example 1:

Input: mat = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], cols = 2
Output: 3
Explanation:
As shown in the diagram above, one possible way of covering 3 rows is by selecting the 0th and 2nd columns.
It can be shown that no more than 3 rows can be covered, so we return 3.
Example 2:

Input: mat = [[1],[0]], cols = 1
Output: 2
Explanation:
Selecting the only column will result in both rows being covered, since the entire matrix is selected.
Therefore, we return 2.

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 12
mat[i][j] is either 0 or 1.
1 <= cols <= n
'''

from typing import List


class Solution:
  def maximumRows(self, mat: List[List[int]], cols: int) -> int:
    m, n = len(mat), len(mat[0])
    rows = [0]*m
    
    for i in range(m):
      for j in range(n):
        if mat[i][j] == 1:
          rows[i] |= (1 << j)
          
    max_count = 0
    # print(rows, 1<<n)
    
    for mask in range(1, 1<<n):
      col_cnt = bin(mask).count('1')
      if col_cnt > cols:
        continue
        
      # print(mask, bin(mask))
      cnt = 0
      
      for r in range(m):
        if rows[r] & mask == rows[r]:
          cnt += 1
          
      max_count = max(max_count, cnt)
    
    return max_count
    