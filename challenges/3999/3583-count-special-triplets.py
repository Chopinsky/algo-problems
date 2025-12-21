'''
3583-count-special-triplets
'''

from typing import List
from collections import defaultdict
from math import comb
from bisect import bisect_left


class Solution:
  def specialTriplets(self, nums: List[int]) -> int:
    pos = defaultdict(list)
    mod = 10**9 + 7

    for i, val in enumerate(nums):
      pos[val].append(i)

    cnt = 0
    if 0 in pos and len(pos[0]) >= 3:
      cnt = comb(len(pos[0]), 3) % mod

    for i, val in enumerate(nums):
      if val == 0 or 2*val not in pos:
        continue

      idx = bisect_left(pos[2*val], i)
      n = len(pos[2*val])
      lcnt = idx
      rcnt = n-idx
      # print('iter:', val, lcnt, rcnt)
      cnt = (cnt + lcnt*rcnt) % mod

    return cnt
    

        