'''
3562-maximum-profit-from-trading-stocks-with-discounts
'''

from typing import List


class Solution:
  def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
    tree = [[] for _ in range(n)]
    dp = [[[0]*(budget+1) for _ in range(2)] for _ in range(n)]

    for u, v in hierarchy:
      tree[u-1].append(v-1)

    def dfs(u: int):
      children = tree[u]
      dps = []

      for v in children:
        dfs(v)
        dps.append((dp[v][0], dp[v][1]))

      for bot in range(2):
        price = present[u]//2 if bot else present[u]
        profit = future[u] - price
        
        # Option 1: not buying u
        base = [0]*(budget+1)
        for c0, _ in dps:
          nxt = [0]*(budget+1)
          for b in range(budget+1):
            if base[b] == 0 and b != 0:
              continue

            for k in range(budget-b+1):
              nxt[b+k] = max(nxt[b+k], base[b] + c0[k])

          base = nxt

        curr = base[:]

        # Option 2: buying u
        if price <= budget:
          base = [0]*(budget+1)
          for _, c1 in dps:
            nxt = [0]*(budget+1)
            for b in range(budget+1):
              if base[b] == 0 and b != 0:
                continue

              for k in range(budget-b+1):
                nxt[b+k] = max(nxt[b+k], base[b] + c1[k])

            base = nxt

          for b in range(price, budget+1):
            curr[b] = max(curr[b], base[b-price]+profit)

        dp[u][bot] = curr

    dfs(0)
    
    return max(dp[0][0])
