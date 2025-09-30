'''
1039-minimum-score-triangulation-of-polygon
'''

from typing import List, Tuple
from functools import cache
import math


class Solution:
  def minScoreTriangulation(self, values: List[int]) -> int:
    @cache
    def dp(vals: Tuple) -> int:
      if not vals:
        return 0

      if len(vals) <= 3:
        res = 1
        for val in vals:
          res *= val

        return res

      n = len(vals)
      res = math.inf
      base = vals[0] * vals[-1]

      for k in range(1, n-1):
        t0 = base * vals[k]

        if k == 1:
          t1 = 0
          t2 = dp(tuple([v for v in vals[1:n]]))

        elif k == n-2:
          t2 = 0
          t1 = dp(tuple([v for v in vals[:k+1]]))

        else:
          t1 = dp(tuple([v for v in vals[:k+1]]))
          t2 = dp(tuple([v for v in vals[k:]]))

        res = min(res, t0+t1+t2)

      return res

    return dp(tuple(values))
        