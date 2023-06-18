'''
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.

Example 1:

Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.

Example 2:

Input: grid = [[1],[2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 10^5
1 <= grid[i][j] <= 10^5
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  def countPaths(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    mod = 10**9 + 7
    stack = sorted([(grid[x][y], x, y) for y in range(n) for x in range(m)])
    count = {(x, y): 1 for x in range(m) for y in range(n)}
    # print(stack, count)
    
    for val, x, y in stack:
      for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] >= val:
          continue
          
        count[x, y] = (count[x, y] + count[x0, y0]) % mod
    
    total = 0
    for x in range(m):
      for y in range(n):
        total = (total + count[x, y]) % mod
        
    return total
        
        
  def countPaths(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[1]*n for _ in range(m)]
    cand = []
    cnt = 0
    
    for i in range(m):
      for j in range(n):
        heappush(cand, (grid[i][j], i, j))
        
    while cand:
      val, x, y = heappop(cand)
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] >= val:
          continue
          
        dp[x][y] += dp[x0][y0]
        
      cnt = (cnt + dp[x][y]) % (10 ** 9 + 7)
    
    return cnt
    