'''
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
'''

from typing import List

class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    def find_head():
      for x in range(m):
        for y in range(n):
          if grid[x][y] == 1:
            return (x, y)
          
      return None
    
    def count(coord: tuple) -> int:
      if not coord:
        return 0
      
      stack = [coord]
      seen = set(stack)
      total = 0
      
      while stack:
        x, y = stack.pop()
        peri = 4
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
            continue
            
          if grid[x0][y0] == 0:
            continue
            
          peri -= 1
          if (x0, y0) in seen:
            continue
            
          seen.add((x0, y0))
          stack.append((x0, y0))
        
        total += peri
        # print((x, y), peri)
        
      return total
      
    return count(find_head())
        