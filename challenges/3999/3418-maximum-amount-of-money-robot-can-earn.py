'''
3418-maximum-amount-of-money-robot-can-earn
'''

import math


class Solution:
  def maximumAmount(self, coins: list[list[int]]) -> int:
    seen = {}
    q = []
    m, n = len(coins), len(coins[0])
    curr = [[-math.inf]*3 for _ in range(n)]
    curr[0][2] = 0
    nxt = []

    for i in range(m):
      for j in range(n):
        val = coins[i][j]
        prev = nxt[-1] if nxt else [-math.inf]*3
        nxt.append([-math.inf]*3)

        for k in range(3):
          left = prev[k]
          up = curr[j][k]

          # take the coin (+/-)
          nxt[j][k] = val + max(left, up)

          # can fight
          if val < 0 and k < 2:
            left = prev[k+1]
            up = curr[j][k+1]
            nxt[j][k] = max(nxt[j][k], left, up)

      curr, nxt = nxt, curr
      nxt.clear()
      # print('iter:', i, curr)

    # print('end:', curr)
    return max(curr[-1])
