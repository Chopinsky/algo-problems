'''
Given a 2D grid consisting of 1s (land) and 0s (water).  An island is a maximal 4-directionally (horizontal or vertical) connected group of 1s.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

 

Example 1:



Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:

Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
Example 3:

Input: grid = [[1,0,1,0]]
Output: 0
Example 4:

Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]]
Output: 1
Example 5:

Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[i].length <= 30
grid[i][j] is 0 or 1.
'''


from typing import List, Tuple


class Solution:
  '''
  the trick is that to divide the sole island into 2 parts, we need to toggle at 
  most 2 lands to the sea -- we can always get a land on the edge by doing so, the
  question is sometimes, there's 1 critical land that connects 2 strongly connected
  components, and we can only remove this 1 land to get the disconnected islands, and
  we shall check if this critical land exists.
  '''
  def minDays(self, grid: List[List[int]]) -> int:
    islands = []
    seen = set()
    critical_lands = {}
    m, n = len(grid), len(grid[0])
    
    def dfs(i: int, j: int) -> Tuple[int, int]:
      seen.add((i, j))  
      stack = [(i, j)]
      min_conn = -1
      count = 0
      
      while stack:
        x, y = stack.pop()
        count += 1
        neighbor = []
        
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or not grid[x0][y0]:
            continue
            
          neighbor.append((x0, y0))
          
          if (x0, y0) in seen:
            continue
            
          seen.add((x0, y0))
          stack.append((x0, y0))
      
        min_conn = len(neighbor) if min_conn < 0 else min(min_conn, len(neighbor))
        if len(neighbor) > 1:
          critical_lands[x, y] = neighbor
      
      return (min_conn, count)
      
    def still_connected(src: Tuple[int, int], nb: List[Tuple[int, int]]) -> bool:
      count = 1
      targets = set(nb)
      stack = [nb[0]]
      visited = set(stack + [src])
      
      while stack:
        x, y = stack.pop()
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
          x0, y0 = x+dx, y+dy
            
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
            continue
            
          if (not grid[x0][y0]) or ((x0, y0) in visited):
            continue
            
          if (x0, y0) in targets:
            count += 1
            
          if count == len(nb):
            return True
            
          visited.add((x0, y0))
          stack.append((x0, y0))
          
      return False
      
    for i in range(m):
      for j in range(n):
        if grid[i][j] and (i, j) not in seen:
          islands.append(dfs(i, j))
          
    # no islands or island is 
    if not islands or len(islands) > 1:
      return 0
    
    # if the sole island has 2 or less lands, must remove all of them
    if islands[0][1] <= 2:
      return islands[0][1]
    
    # print(islands, critical_lands)
    for src, nb in critical_lands.items():
      for land in nb:
        if (land not in critical_lands) or (len(critical_lands[land]) == 1):
          return 1
        
      if not still_connected(src, nb):
        # print('disconnect', src, nb)
        return 1
    
    return 2
  