'''
3572-maximize-ysum-by-picking-a-triplet-of-distinct-xvalues
'''

from typing import List


class Solution:
  def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
    vals = {}
    for vx, vy in zip(x, y):
      vals[vx] = max(vals.get(vx, 0), vy)

    # print('init:', vals)
    if len(vals) < 3:
      return -1

    s = sorted(vals.values())
    return sum(s[-3:])
        