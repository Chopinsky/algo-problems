'''
3741-minimum-distance-between-three-equal-elements-ii
'''

from typing import List
from collections import defaultdict


class Solution:
  def minimumDistance(self, nums: List[int]) -> int:
    pos = defaultdict(list)
    n = len(nums)
    dist = -1

    for i in range(n):
      val = nums[i]
      lst = pos[val]
      lst.append(i)

      if len(lst) >= 3:
        d = abs(lst[-1]-lst[-2]) + abs(lst[-2]-lst[-3]) + abs(lst[-1]-lst[-3])
        if dist < 0 or d < dist:
          dist = d

    return dist
