'''
3592-inverse-coin-change
'''

from typing import List
from functools import cache


class Solution:
  def findCoins(self, numWays: List[int]) -> List[int]:
    coins = []

    @cache
    def count_ways(val: int, i: int) -> int:
      if val == 0:
        return 1

      if i < 0:
        return 0

      curr = coins[i]
      ways = 0

      while val >= 0:
        ways += count_ways(val, i-1)
        val -= curr

      return ways 

    for i, c in enumerate(numWays):
      ways = count_ways(i+1, len(coins)-1)
      # print('iter:', coins, (i+1, c), ways, ways==c, ways+1==c)

      # can do with coins
      if ways == c:
        continue

      # new coin discovered
      if ways+1 == c:
        coins.append(i+1)
        continue

      # illegal case discovered
      return []

    return coins

