'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''


from typing import List


class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    if grid[0][0] != 0 or grid[-1][-1] != 0:
      return -1

    m, n = len(grid), len(grid[0])
    if m == 1 and n == 1:
      return 1
    
    curr, nxt = [(0, 0)], []
    seen = set(curr)
    ln = 1
    
    while curr:
      # print(ln, curr)
      ln += 1
      
      for x0, y0 in curr:
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
          x1, y1 = x0+dx, y0+dy
          if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n or grid[x1][y1] != 0 or (x1, y1) in seen:
            continue
          
          if x1 == m-1 and y1 == n-1:
            return ln
          
          seen.add((x1, y1))
          nxt.append((x1, y1))
          
      curr, nxt = nxt, curr
      nxt.clear()
    
    return -1
          
        
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    if grid[m-1][n-1] == 1 or grid[0][0] == 1:
      return -1
    
    if m == 1 and n == 1:
      return 1
      
    stack, nxt = [(0, 0)], []
    visited = set(stack)
    steps = 1
    
    while stack:
      steps += 1
      
      for x, y in stack:
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] != 0:
            continue
            
          if (x0, y0) in visited:
            continue
            
          if x0 == m-1 and y0 == n-1:
            return steps
          
          visited.add((x0, y0))
          nxt.append((x0, y0))
        
      stack, nxt = nxt, stack
      nxt.clear()
      
    return -1
        