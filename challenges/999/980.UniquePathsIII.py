'''
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
'''


from typing import List


class Solution:
  def uniquePathsIII(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    stack = []
    target = 0
    end = None
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == -1:
          continue
          
        key = 1 << (i*n + j)
        if grid[i][j] == 1:
          stack.append((i, j, key))
          
        if grid[i][j] == 2:
          end = (i, j)
        
        target |= key
        
    count = 0
    # print(format(target, '#020b'))
    
    while stack:
      x, y, seen = stack.pop()
      if (x, y) == end and seen == target:
        count += 1
        continue
        
      for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] == -1:
          continue
          
        key = 1 << (x0*n + y0)
        if seen & key > 0:
          continue
          
        stack.append((x0, y0, seen | key))
    
    return count
  