'''
3801-minimum-cost-to-merge-sorted-lists
'''

from typing import List
import math
from functools import cache


class Solution:
  def minMergeCost(self, l: List[List[int]]) -> int:
    n = len(l)

    @cache
    def calc_len(m: int) -> int:
      i = 0
      ln = 0

      while m > 0 and i < n:
        if m&1 > 0:
          ln += len(l[i])

        i += 1
        m >>= 1

      return ln

    @cache
    def find_median(m: int):
      i = 0
      nums = []

      while m > 0 and i < n:
        if m&1 > 0:
          nums += l[i]

        i += 1
        m >>= 1

      nums.sort()
      mid = (len(nums)-1)//2

      return nums[mid]
        
    def calc_cost(ma: int, mb: int):
      la = calc_len(ma)
      lb = calc_len(mb)
      mva = find_median(ma)
      mvb = find_median(mb)
      # print('cost:', bin(ma), bin(mb), la, lb, (mva, mvb))

      return la + lb + abs(mva-mvb)

    dp = {0:0}
    top = (1<<n)-1

    for m in range(1, top+1):
      if bin(m).count('1') == 1:
        dp[m] = 0
        continue

      # init
      dp[m] = math.inf
      # print('start:', m, bin(m))

      s0 = m
      s0 = (s0-1)&m

      while s0 > 0:
        s1 = m^s0
        if s1 > s0:
          break

        # print('inner:', (s0, s1), (bin(s0), bin(s1)))

        dp[m] = min(
          dp[m],
          dp[s0]+dp[s1]+calc_cost(s0, s1)
        )

        # get the next submask
        s0 = (s0-1)&m
        
      # print('iter:', m, dp[m])

    return dp[top]
