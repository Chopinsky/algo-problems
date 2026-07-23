'''
3633-earliest-finish-time-for-land-and-water-rides-i
'''

import math
from typing import List


class Solution:
  def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
    land = sorted(zip(landStartTime, landDuration))
    water = sorted(zip(waterStartTime, waterDuration))

    def tour(first: list, second: list) -> int:
      early = math.inf
      r1 = sorted(sum(t) for t in first)
      r2_started = second
      r2_not_started = [sum(t) for t in second]
      n2 = len(second)

      for i in range(n2-2, -1, -1):
        r2_not_started[i] = min(r2_not_started[i], r2_not_started[i+1])

      i = 0
      for t1 in r1:
        t2 = math.inf
        while i < n2 and r2_started[i][0] <= t1:
          t2 = min(t2, r2_started[i][1])
          i += 1

        if t2 < math.inf:
          early = min(early, t1+t2)

        if i < n2:
          early = min(early, r2_not_started[i])

      return early

    return min(
      tour(land, water),
      tour(water, land),
    )
        