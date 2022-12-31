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

from functools import lru_cache
from typing import List


class Solution:
  def uniquePathsIII(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    x0, y0, tkey = -1, -1, -1
    target = 0
    
    def to_key(x: int, y: int) -> int:
      return x*n + y
    
    @lru_cache(None)
    def count_visited_nodes(mask: int) -> int:
      cnt = 0
      while mask > 0:
        if mask & 1:
          cnt += 1
          
        mask >>= 1
          
      return cnt
    
    for x in range(m):
      for y in range(n):
        if grid[x][y] == -1:
          continue
          
        target += 1
        if grid[x][y] == 1:
          x0, y0 = x, y
          
        if grid[x][y] == 2:
          tkey = 1 << to_key(x, y)
          
    # print((x0, y0), bin(tkey), target)
    if x0 < 0 or y0 < 0 or tkey < 0:
      return 0
    
    @lru_cache(None)
    def dp(x: int, y: int, mask: int) -> int:
      key = 1 << to_key(x, y)
      # print('visit:', x, y, bin(key), bin(mask))
      
      # already visited
      if key & mask > 0:
        return 0
      
      mask |= key
      if key == tkey:
        # print('done:', x, y, count_visited_nodes(nxt_mask))
        return 1 if count_visited_nodes(mask) == target else 0
      
      ways = 0
      for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        xx, yy = x+dx, y+dy
        if xx < 0 or xx >= m or yy < 0 or yy >= n or grid[xx][yy] < 0:
          continue
          
        ways += dp(xx, yy, mask)
      
      return ways
    
    return dp(x0, y0, 0)
    

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
  