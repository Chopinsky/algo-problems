'''
3864-minimum-cost-to-partition-a-binary-string
'''

from functools import cache
from math import inf


class Solution:
  def minCost(self, s: str, encCost: int, flatCost: int) -> int:
    n = len(s)
    ones = [0]*n
    
    for i in range(n):
      ones[i] = (1 if s[i] == "1" else 0) + (ones[i-1] if i > 0 else 0)

    def cnt_x(i: int, j: int) -> int:
      return ones[j] - (ones[i-1] if i > 0 else 0)

    @cache
    def calc_seg(i: int, j: int) -> int:
      cx = cnt_x(i, j)
      if cx == 0:
        return flatCost

      ln = j-i+1
      v0 = ln * cx * encCost
      v1 = inf

      # can split
      if ln%2 == 0:
        mid = (i+j-1)//2
        v1 = calc_seg(i, mid) + calc_seg(mid+1, j)

      return min(v0, v1)

    return calc_seg(0, n-1)
        