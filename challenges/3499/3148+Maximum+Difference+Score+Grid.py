'''
3148. Maximum Difference Score in a Grid

You are given an m x n matrix grid consisting of positive integers. You can move from a cell in the matrix to any other cell that is either to the bottom or to the right (not necessarily adjacent). The score of a move from a cell with the value c1 to a cell with the value c2 is c2 - c1.
You can start at any cell, and you have to make at least one move.

Return the maximum total score you can achieve.

Example 1:

Input: grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]

Output: 9

Explanation: We start at the cell (0, 1), and we perform the following moves:
- Move from the cell (0, 1) to (2, 1) with a score of 7 - 5 = 2.
- Move from the cell (2, 1) to (2, 2) with a score of 14 - 7 = 7.
The total score is 2 + 7 = 9.

Example 2:

Input: grid = [[4,3,2],[3,2,1]]

Output: -1

Explanation: We start at the cell (0, 0), and we perform one move: (0, 0) to (0, 1). The score is 3 - 4 = -1.

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 10^5
1 <= grid[i][j] <= 10^5
'''

from typing import List

class Solution:
  def maxScore(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    scores = [[0 for val in row] for row in grid]
    vals = [row.copy() for row in grid]
    top_score = -float('inf')
    diff = -float('inf')
    has_moves = False
    
    for i in range(m-1, -1, -1):
      for j in range(n-1, -1, -1):
        val = grid[i][j]
        if i == m-1 and j == n-1:
          scores[i][j] = val
          continue
        
        score = scores[i][j]
        max_val = -1
        if i < m-1:
          score = max(score, -val+scores[i+1][j])
          max_val = max(max_val, vals[i+1][j])
          
        if j < n-1:
          score = max(score, -val+scores[i][j+1])
          max_val = max(max_val, vals[i][j+1])
        
        has_moves = has_moves or val <= max_val
        top_score = max(top_score, score)
        diff = max(diff, max_val-val)
        vals[i][j] = max(vals[i][j], max_val)
        scores[i][j] = score+val
        # print((i, j), val, max_val, score)
    
    return top_score if has_moves else diff
    