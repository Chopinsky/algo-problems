'''
3332-maximum-points-tourist-can-earn
'''

from functools import cache
from typing import List


class Solution:
  def maxScore(self, n: int, k: int, stay: List[List[int]], travel: List[List[int]]) -> int:
    @cache
    def dp(i: int, curr: int) -> int:
      if i >= k:
        return 0

      # if stay:
      # print('at:', (i, curr))
      val = stay[i][curr] + dp(i+1, curr)

      # if travel to dest
      for dest in range(n):
        if curr == dest:
          continue

        val = max(val, travel[curr][dest] + dp(i+1, dest))

      return val

    return max(dp(0, c) for c in range(n))
        