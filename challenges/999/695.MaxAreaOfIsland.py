'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
'''

from typing import List


class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    dirs = [-1, 0, 1, 0, -1]
    h, w = len(grid), len(grid[0])
    ans = 0

    def area(x: int, y: int) -> int:
      stack = [(x, y)]
      island = 0

      while len(stack) > 0:
        (x0, y0), stack = stack[0], stack[1:]
        if grid[x0][y0] == 0:
          continue

        grid[x0][y0] = 0
        island += 1

        for i in range(4):
          x1, y1 = x0+dirs[i], y0+dirs[i+1]

          if x1 < 0 or x1 >= h or y1 < 0 or y1 >= w or grid[x1][y1] == 0:
            continue

          stack.append((x1, y1))

      return island

    for i in range(h):
      for j in range(w):
        if grid[i][j] == 1:
          ans = max(ans, area(i, j))

    return ans
