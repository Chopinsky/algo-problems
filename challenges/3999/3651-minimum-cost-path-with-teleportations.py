'''
3651-minimum-cost-path-with-teleportations
'''

import math
from typing import List


class Solution:
  def minCost(self, grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    top_val = grid[0][0]
    dp = [
      [
        [
          math.inf for _ in range(k+1)
        ] for _ in range(n)
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

    # calc best cost at each additional teleport
    for tc in range(1, k+1):
      min_cost_v = [math.inf] * (top_val+2)
      for i in range(m):
        for j in range(n):
          min_cost_v[grid[i][j]] = min(
            min_cost_v[grid[i][j]],   # current best
            dp[i][j][tc-1],           # best score after teleporting tc-1 times
          )

      # aggregate to get the best from all above values, given
      # the teleport cost is 0
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
