'''
You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

Example 1:
https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82045-am.png

Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.

Example 2:
https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82050-am.png

Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.
 

Constraints:

m == isWater.length
n == isWater[i].length
1 <= m, n <= 1000
isWater[i][j] is 0 or 1.
There is at least one water cell.
'''

from typing import List


class Solution:
  def highestPeak(self, mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    curr, nxt = set(), set()
    seen = set()
    # print(res)
    
    for i in range(m):
      for j in range(n):
        if mat[i][j] == 1:
          mat[i][j] = 0
          curr.add((i, j))
        else:
          mat[i][j] = float('inf')
          
    while curr:
      # print(curr)
      seen |= curr
      for x, y in curr:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or mat[x0][y0] == 0 or (x0, y0) in seen:
            continue
          
          mat[x0][y0] = min(mat[x0][y0], 1+mat[x][y])
          nxt.add((x0, y0))
          
      curr, nxt = nxt, curr
      nxt.clear()
    
    return mat
    