'''
3740-minimum-distance-between-three-equal-elements-i
'''

from typing import List
from collections import defaultdict


class Solution:
  def minimumDistance(self, nums: List[int]) -> int:
    n = len(nums)
    dist = -1
    pos = defaultdict(list)

    for i, val in enumerate(nums):
      pos[val].append(i)

      if len(pos[val]) >= 3:
        a, b, c = pos[val][-3:]
        d0 = abs(a-b) + abs(b-c) + abs(a-c)
        if dist < 0 or d0 < dist:
          dist = d0
    
    return dist
