'''
3651-minimum-cost-path-with-teleportations
'''

import math
from typing import List


class Solution:
  def minCost(self, grid: List[List[int]], k: int) -> int:
    n = len(grid)
    m = len(grid[0])
    cost = [[math.inf] * m for _ in range(n)] # cost[i][j] = minimum cost to reach destination from (i, j)
    cost[-1][-1] = 0
    tcost = [math.inf] * (max(max(row) for row in grid) + 1)

    for t in range(k + 1):
      for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
          # move right, down, or teleport
          if i < n - 1: 
            cost[i][j] = min(cost[i][j], cost[i+1][j] + grid[i+1][j])

          if j < m - 1: 
            cost[i][j] = min(cost[i][j], cost[i][j+1] + grid[i][j+1])

          if t > 0: 
            cost[i][j] = min(cost[i][j], tcost[grid[i][j]])
      
      # compute tcost for next t
      for i in range(n):
        for j in range(m):
          tcost[grid[i][j]] = min(tcost[grid[i][j]], cost[i][j])

      for i in range(1, len(tcost)): 
        tcost[i] = min(tcost[i], tcost[i - 1]) # compute pref min
    
    return cost[0][0]

  def minCost(self, grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    top_val = grid[0][0]

    # [m][n][k+1] matrix (0 to k teleport)
    dp = [
      [
        [math.inf for _ in range(k+1)] for _ in range(n)
      ] for _ in range(m)
    ]

    # init dp, no teleport
    for i in range(m):
      for j in range(n):
        top_val = max(top_val, grid[i][j])

        if i == 0 and j == 0:
          dp[i][j][0] = 0
          continue

        dp[i][j][0] = min(
          dp[i-1][j][0] if i > 0 else math.inf,
          dp[i][j-1][0] if j > 0 else math.inf,
        ) + grid[i][j]

    # print('init:', dp, dp[-1][-1][k])

    # calc cost at each teleport
    for tc in range(1, k+1):
      min_cost_v = [math.inf] * (top_val+2)
      for i in range(m):
        for j in range(n):
          min_cost_v[grid[i][j]] = min(
            min_cost_v[grid[i][j]],
            dp[i][j][tc-1],
          )

      min_cost_above_v = [math.inf] * (top_val+2)
      for v in range(top_val, -1, -1):
        min_cost_above_v[v] = min(
          min_cost_above_v[v+1],
          min_cost_v[v],
        )

      for i in range(m):
        for j in range(n):
          dp[i][j][tc] = min(
            (dp[i-1][j][tc] + grid[i][j]) if i > 0 else math.inf,
            (dp[i][j-1][tc] + grid[i][j]) if j > 0 else math.inf,
            min_cost_above_v[grid[i][j]],
          )

    # print('done:', dp, dp[-1][-1][k])
    return dp[-1][-1][k]
