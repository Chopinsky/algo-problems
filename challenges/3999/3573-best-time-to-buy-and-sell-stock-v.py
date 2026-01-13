'''
3573-best-time-to-buy-and-sell-stock-v
'''

from typing import List
from math import inf


class Solution:
  def maximumProfit(self, prices: List[int], k: int) -> int:
    b = [-inf] * k
    s = [0] * k
    res = [0] * (k+1)

    for p in prices:
      for j in range(k, 0, -1):
        res[j] = max(res[j], b[j-1]+p, s[j-1]-p)
        b[j-1] = max(b[j-1], res[j-1]-p)
        s[j-1] = max(s[j-1], res[j-1]+p)

    return max(res)
        