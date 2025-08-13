'''
3623-count-number-of-trapezoids-i
'''

from math import comb
from typing import List
from collections import defaultdict


class Solution:
  def countTrapezoids(self, points: List[List[int]]) -> int:
    mod = 10**9 + 7
    ys = defaultdict(int)
    cnt, pairs = 0, 0

    for _, y in points:
      ys[y] += 1

    for y in sorted(ys):
      points = ys[y]
      if points <= 1:
        continue

      p0 = comb(points, 2)
      cnt = (cnt + pairs*p0) % mod
      pairs = (pairs + p0) % mod

    return cnt
        