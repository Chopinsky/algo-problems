'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
'''


from typing import List


class Solution:
  def largestIsland(self, grid: List[List[int]]) -> int:
    h, w = len(grid), len(grid[0])
    dirs = [-1, 0, 1, 0, -1]
    edges = set()
    islands = [[0 for _ in range(w)] for _ in range(h)]
    idx = 1
    
    def mark(x: int, y: int) -> int:
      nonlocal h, w, idx
      stack = [(x,y)]
      area = 0
      
      while len(stack) > 0:
        x0, y0 = stack.pop()
        if islands[x0][y0] > 0:
          continue
          
        islands[x0][y0] = idx
        area += 1
        
        for i in range(4):
          x1, y1 = x0+dirs[i], y0+dirs[i+1]
          if x1 < 0 or x1 >= h or y1 < 0 or y1 >= w or islands[x1][y1] > 0:
            continue
            
          if grid[x1][y1] == 0:
            edges.add((x1, y1))
            continue
            
          stack.append((x1, y1))
          
      return area
      
    areas = {}
    largest = 1
    
    for i in range(h):
      for j in range(w):
        if islands[i][j] > 0 or grid[i][j] == 0:
          continue
          
        areas[idx] = mark(i, j)
        largest = max(largest, areas[idx])
        idx += 1
    
    # print(islands, edges, largest)
    
    for ex, ey in edges:
      ni = set()
      for i in range(4):
        x0, y0 = ex+dirs[i], ey+dirs[i+1]
        if x0 < 0 or x0 >= h or y0 < 0 or y0 >= w or grid[x0][y0] == 0:
          continue
        
        ni.add(islands[x0][y0])
        
      count = 1
      for i in ni:
        count += areas[i]
        
      largest = max(count, largest)
    
    return largest
  