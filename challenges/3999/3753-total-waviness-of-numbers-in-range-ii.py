'''
3753-total-waviness-of-numbers-in-range-ii
'''

from typing import Tuple
from functools import cache


class Solution:
  def totalWaviness(self, num1: int, num2: int) -> int:
    def total_waves(num: int) -> int:
      digits = [int(c) for c in str(num)]
      ln = len(digits)

      @cache
      def dfs(i: int, p1, p2, tight: bool, started: bool) -> Tuple[int, int]:
        if i == ln:
          return 0, 1

        max_d = digits[i] if tight else 9
        total = 0
        count = 0

        for d in range(max_d+1):
          nxt_tight = tight and (d == digits[i])
          nxt_started = started or (d != 0)

          if not nxt_started:
            nd1, nd2 = None, None
          elif not started:
            nd1, nd2 = d, None
          else:
            nd1, nd2 = d, p1

          sub_wave, sub_cnt = dfs(
            i+1, nd1, nd2, nxt_tight, nxt_started
          )

          total += sub_wave
          count += sub_cnt

          if started and nxt_started and p1 is not None and p2 is not None:
            if (p2 < p1 and d < p1) or (p1 < p2 and p1 < d):
              total += sub_cnt

        return total, count

      return dfs(0, None, None, True, False)[0]

    w1 = total_waves(num1-1)   
    w2 = total_waves(num2)

    return w2-w1
        