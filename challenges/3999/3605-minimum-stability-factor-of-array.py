'''
3605-minimum-stability-factor-of-array
'''

from typing import List
from math import gcd


class Solution:
  def minStable(self, nums: List[int], maxC: int) -> int:
    n = len(nums)
    l, r = 0, n+1
    last = r

    def count(ln: int) -> int:
      ops = 0
      i = 0

      while i+ln-1 < n:
        curr = nums[i]
        j = i+1
        # print('count:', ln, (i, j))

        while j < i+ln and curr > 1:
          curr = gcd(curr, nums[j])
          j += 1

        # subarray is stable, gcd > 1, make 1 change
        if curr > 1:
          ops += 1
          i += ln
        else:
          i += 1

      return ops

    while l+1 < r:
      mid = (l+r) // 2
      # print('iter:', (l, r, mid), count(mid))
      if count(mid) <= maxC:
        r = mid
      else:
        l = mid

    return l
