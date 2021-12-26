'''
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
'''


from typing import List


class Solution:
  def shortestBridge(self, grid: List[List[int]]) -> int:
    n = len(grid)
    island = set()
    
    for i in range(n):
      for j in range(n):
        if grid[i][j] == 1:
          island.add((i, j))
          break
          
      if island:
        break
          
    stack = list(island)
    
    while stack:
      x, y = stack.pop()
      for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= n or y0 < 0 or y0 >= n or not grid[x0][y0] or (x0, y0) in island:
          continue
          
        stack.append((x0, y0))
        island.add((x0, y0))
    
    steps = 0
    stack, nxt = island.copy(), set()
    # print('init', stack, island)
    
    while stack:
      for x, y in stack:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
          x0, y0 = x+dx, y+dy
          
          if x0 < 0 or x0 >= n or y0 < 0 or y0 >= n:
            continue
            
          # print(steps, (x, y), (x0, y0))
          if grid[x0][y0] == 1 and (x0, y0) not in island:
            return steps
          
          if grid[x0][y0] == 0:
            nxt.add((x0, y0))
            island.add((x0, y0))
        
      # print(steps, nxt)
      stack, nxt = nxt, stack
      nxt.clear()
      steps += 1
    
    return steps
  