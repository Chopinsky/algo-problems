'''
3413-maximum-coins-from-k-consecutive-bags
'''

from typing import List
from bisect import bisect_right


class Solution:
  def maximumCoins(self, coins: List[List[int]], k: int) -> int:
    n = len(coins)
    coins.sort()
    start = [l for l, _, _ in coins]
    end = [r for _, r, _ in coins]
    prefix = [c*(r-l+1) for l, r, c in coins]
    for i in range(1, n):
      prefix[i] += prefix[i-1]

    def get_prefix(i: int) -> int:
      if i < 0:
        return 0

      total = 0
      rdx = bisect_right(end, i)-1
      if rdx >= 0:
        total += prefix[rdx]

      ldx = bisect_right(start, i)-1
      if ldx > rdx:
        s, _, c = coins[ldx]
        total += (i-s+1)*c

      # print('find:', i, total)
      return total

    def get_coins(l: int, r: int) -> int:
      return get_prefix(r) - get_prefix(l-1)

    max_coins = 0
    candid = sorted(set(start + [r-k+1 for r in end]))
    # print('init:', coins, prefix, candid)

    for s in candid:
      max_coins = max(max_coins, get_coins(s, s+k-1))

    return max_coins
