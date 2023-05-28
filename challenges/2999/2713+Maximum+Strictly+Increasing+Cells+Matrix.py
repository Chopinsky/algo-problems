'''
2713. Maximum Strictly Increasing Cells in a Matrix

Given a 1-indexed m x n integer matrix mat, you can select any cell in the matrix as your starting cell.

From the starting cell, you can move to any other cell in the same row or column, but only if the value of the destination cell is strictly greater than the value of the current cell. You can repeat this process as many times as possible, moving from cell to cell until you can no longer make any moves.

Your task is to find the maximum number of cells that you can visit in the matrix by starting from some cell.

Return an integer denoting the maximum number of cells that can be visited.

Example 1:

Input: mat = [[3,1],[3,4]]
Output: 2
Explanation: The image shows how we can visit 2 cells starting from row 1, column 2. It can be shown that we cannot visit more than 2 cells no matter where we start from, so the answer is 2. 
Example 2:

Input: mat = [[1,1],[1,1]]
Output: 1
Explanation: Since the cells must be strictly increasing, we can only visit one cell in this example. 
Example 3:

Input: mat = [[3,1,6],[-9,5,7]]
Output: 4
Explanation: The image above shows how we can visit 4 cells starting from row 2, column 1. It can be shown that we cannot visit more than 4 cells no matter where we start from, so the answer is 4. 

Constraints:

m == mat.length 
n == mat[i].length 
1 <= m, n <= 10^5
1 <= m * n <= 10^5
-10^5 <= mat[i][j] <= 10^5
'''

import math
from typing import List
from collections import defaultdict


class Solution:
  def maxIncreasingCells(self, mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    points = []
    
    for i in range(m):
      for j in range(n):
        points.append((mat[i][j], i, j))
    
    points.sort()
    # print(points)
    
    rows = defaultdict(int)
    cols = defaultdict(int)
    nr, nc = defaultdict(int), defaultdict(int)
    curr_val = math.inf
    
    def merge():
      for r, cnt in nr.items():
        rows[r] = max(rows[r], cnt)
          
      for c, cnt in nc.items():
        cols[c] = max(cols[c], cnt)

      nr.clear()
      nc.clear()
    
    while points:
      val, x, y = points.pop()
      
      if val != curr_val:
        merge()
        curr_val = val
      
      cnt = max(rows[x]+1, cols[y]+1)
      nr[x] = max(nr[x], cnt)
      nc[y] = max(nc[y], cnt)
      
      # print('post ==>', (val, x, y), curr_val)
      # print(rows, cols)
      # print(nr, nc)
    
    merge()
    # print('fin:', rows, cols)
    
    return max(max(rows.values()), max(cols.values()))
    