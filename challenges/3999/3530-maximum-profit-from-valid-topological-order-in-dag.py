'''
3530-maximum-profit-from-valid-topological-order-in-dag
'''

from typing import List


class Solution:
  def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
    pre = [0]*n
    for i, j in edges:
      pre[j] |= (1 << i)

    dp = [-1]*(1<<n)
    dp[0] = 0

    for mask in range(1<<n):
      if dp[mask] == -1:
        continue

      pos = mask.bit_count() + 1
      for i in range(n):
        if (mask>>i) & 1 == 1:
          continue

        # all pre nodes have been visited
        if (mask & pre[i]) == pre[i]:
          nxt_mask = mask | (1 << i)
          dp[nxt_mask] = max(
            dp[nxt_mask],
            dp[mask] + score[i]*pos
          )

    return dp[(1<<n)-1]

        