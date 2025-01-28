'''
2658. Maximum Number of Fish in a Grid

You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Example 1:

Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
'''

from typing import List


class Solution:
  def findMaxFish(self, grid: List[List[int]]) -> int:
    seen = set()
    m, n = len(grid), len(grid[0])
    fish = 0

    def dfs(x: int, y: int) -> int:
      pool = grid[x][y]
      stack = [(x, y)]

      while stack:
        x0, y0 = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x1, y1 = x0+dx, y0+dy
          if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
            continue

          if (x1, y1) in seen or grid[x1][y1] == 0:
            continue

          seen.add((x1, y1))
          pool += grid[x1][y1]
          stack.append((x1, y1))

      # print('done:', (x, y), pool)

      return pool

    for x in range(m):
      for y in range(n):
        if (x, y) in seen or grid[x][y] == 0:
          continue

        seen.add((x, y))
        fish = max(fish, dfs(x, y))

    return fish
        
  def findMaxFish(self, grid: List[List[int]]) -> int:
    seen = set()
    m, n = len(grid), len(grid[0])
    
    def dfs(x, y):
      # print('start:', (x, y))
      cnt = grid[x][y]
      stack = [(x, y)]
      seen.add((x, y))
      
      while stack:
        r, c = stack.pop()
        
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
          r0, c0 = r+dr, c+dc
          if r0 < 0 or r0 >= m or c0 < 0 or c0 >= n or ((r0, c0) in seen) or (grid[r0][c0] == 0):
            continue
            
          seen.add((r0, c0))
          cnt += grid[r0][c0]
          stack.append((r0, c0))
          # print((x, y), (r0, c0))
          
      return cnt
    
    catch = 0
    for x in range(m):
      for y in range(n):
        if grid[x][y] == 0 or (x, y) in seen:
          continue
          
        catch = max(catch, dfs(x, y))
        
    return catch
    