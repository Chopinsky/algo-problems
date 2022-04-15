'''
You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if they have the same color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

You should color the border of the connected component that contains the square grid[row][col] with color.

Return the final grid.

Example 1:

Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
Output: [[3,3],[3,2]]
Example 2:

Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
Output: [[1,3,3],[2,3,3]]
Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
Output: [[2,2,2],[2,1,2],[2,2,2]]
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j], color <= 1000
0 <= row < m
0 <= col < n
'''

from typing import List


class Solution:
  def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    base = grid[row][col]
    
    comp = set()
    border = set()
    stack, nxt = [(row, col)], []
    
    while stack:
      for x, y in stack:
        if x == 0 or x == m-1 or y == 0 or y == n-1:
          border.add((x, y))
          
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
            continue
            
          if (x0, y0) in comp: 
            continue
            
          if grid[x0][y0] != base:
            border.add((x, y))
            continue
            
          nxt.append((x0, y0))
          comp.add((x0, y0))
          
      stack, nxt = nxt, stack
      nxt.clear()
      
    # print(comp, border)
    for x, y in border:
      grid[x][y] = color
    
    return grid
        