'''
3761-minimum-absolute-distance-between-mirror-pairs
'''

from typing import List
from functools import cache
from collections import defaultdict
from bisect import bisect_left


class Solution:
  def minMirrorPairDistance(self, nums: List[int]) -> int:
    idx = defaultdict(list)
    dist = -1

    @cache
    def rev(src: int) -> int:
      val = 0
      while src > 0:
        val = 10*val + src%10
        src //= 10

      return val

    for i, val in enumerate(nums):
      idx[int(val)].append(i)

    # print('init:', idx)
    for i, v0 in enumerate(nums):
      v1 = rev(v0)
      if v1 not in idx:
        continue

      lst = idx[v1]
      j = bisect_left(lst, i)
      if v0 == v1:
        j -= 1

      if 0 <= j < len(lst):
        d0 = abs(i-lst[j])
        if dist < 0 or d0 < dist:
          dist = d0

      if v0 == v1:
        j += 1

      if j+1 < len(lst):
        d1 = abs(i-lst[j+1])
        if dist < 0 or d1 < dist:
          dist = d1

    return dist

  def minMirrorPairDistance(self, nums: List[int]) -> int:
    res = -1
    last = {}

    for i, val in enumerate(nums):
      if val in last:
        dist = i-last[val]
        res = dist if res < 0 else min(res, dist)

      rval = int(str(val)[::-1])
      # print('iter:', val, rval)
      last[rval] = i

    return res
