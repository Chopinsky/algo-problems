'''
3429-paint-house-iv
'''

from typing import List
from collections import defaultdict


class Solution:
  def minCost(self, n: int, cost: List[List[int]]) -> int:
    curr, nxt = defaultdict(int), defaultdict(int)
    m, n = len(cost), len(cost[0])

    for i in range(n):
      for j in range(n):
        if i == j:
          continue

        curr[i, j] = 0

    # print('init:', curr)
    init_cost = float('inf')

    for k in range(m//2):
      for i0 in range(n):
        for j0 in range(n):
          if i0 == j0:
            continue

          c = init_cost
          c0 = cost[k][i0]
          c1 = cost[m-1-k][j0]

          for i1, j1 in curr:
            if i0 == i1 or j0 == j1:
              continue

            c = min(c, c0+c1+curr[i1, j1])

          nxt[i0, j0] = c

      curr, nxt = nxt, curr
      nxt.clear()
      # print('iter:', curr)

    return min(curr.values())
        