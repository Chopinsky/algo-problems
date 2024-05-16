'''
2812. Find the Safest Path in a Grid

You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

Example 1:

Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 0
Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).
Example 2:


Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
Example 3:


Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

Constraints:

1 <= grid.length == n <= 400
grid[i].length == n
grid[i][j] is either 0 or 1.
There is at least one thief in the grid.
'''

from typing import List
from heapq import heappush, heappop

class Solution:
  def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
      return 0
    
    min_dist = [[float('inf')]*n for _ in range(n)]
    cand, nxt = [], []
    
    for i in range(n):
      for j in range(n):
        if grid[i][j] == 1:
          cand.append((i, j))
    
    if not cand:
      return -1
    
    seen = set(cand)
    for x, y in cand:
      min_dist[x][y] = 0
    
    while cand:
      for x, y in cand:
        dist = min_dist[x][y]
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x0 = x + dx
          y0 = y + dy
          if x0 < 0 or x0 >= n or y0 < 0 or y0 >= n:
            continue
            
          min_dist[x0][y0] = min(min_dist[x0][y0], dist+1)

          if (x0, y0) not in seen:
            nxt.append((x0, y0))
            seen.add((x0, y0))
      
      cand, nxt = nxt, cand
      nxt.clear()
    
    # print(min_dist)
    stack = [(-min_dist[0][0], 0, 0)]
    seen.clear()
    seen.add((0, 0))
    
    while stack:
      dist, x, y = heappop(stack)
      if x == n-1 and y == n-1:
        return -dist
      
      if dist == 0:
        return 0
      
      # print((x, y, dist), stack)
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x0 = x + dx
        y0 = y + dy
        if x0 < 0 or x0 >= n or y0 < 0 or y0 >= n:
          continue
          
        if (x0, y0) in seen or grid[x0][y0] == 1:
          continue
          
        dist0 = min(-dist, min_dist[x0][y0])
        heappush(stack, (-dist0, x0, y0))
        seen.add((x0, y0))
        # print('add:', (x0, y0, dist0))
    
    return 0
  
  def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
      return 0
    
    safe_factor = [[0]*n for _ in range(m)]
    curr, nxt = [(x, y) for y in range(n) for x in range(m) if grid[x][y] == 1], []
    seen = set(curr)
    d = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # print('thieves:', curr)
    
    while curr:
      d += 1
      for x, y in curr:
        for dx, dy in directions:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
            continue
          
          if (x0, y0) in seen:
            continue
            
          seen.add((x0, y0))
          nxt.append((x0, y0))
          safe_factor[x0][y0] = d
      
      curr, nxt = nxt, curr
      nxt.clear()

    # print('sf:', safe_factor)
    path = [[-1]*n for _ in range(m)]
    path[0][0] = safe_factor[0][0]
    stack = [(-path[0][0], 0, 0)]
    
    while stack:
      d, x, y = heappop(stack)
      d = -d
      # print('check:', (x, y), d)
      
      for dx, dy in directions:
        x0, y0 = x+dx, y+dy
        
        # out of the grid
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
          continue
          
        # not going to have a better solution
        if path[x0][y0] >= 0:
          continue
          
        d0 = min(d, safe_factor[x0][y0])
        # print('move', (x0, y0), d0)
        
        path[x0][y0] = d0
        heappush(stack, (-d0, x0, y0))
    
    # print(path)
    return max(0, path[-1][-1])
        