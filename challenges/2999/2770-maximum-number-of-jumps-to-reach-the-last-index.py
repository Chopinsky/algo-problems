'''
2770-maximum-number-of-jumps-to-reach-the-last-index
'''

from typing import List
from math import inf


class Solution:
  def maximumJumps(self, nums: List[int], target: int) -> int:
    n = len(nums)
    steps = [-1]*n
    steps[0] = 0

    for i in range(n):
      if steps[i] < 0:
        continue

      for j in range(i+1, n):
        if abs(nums[j]-nums[i]) <= target:
          steps[j] = max(steps[j], steps[i]+1)

    # print('done:', steps)
    return -1 if steps[-1] == inf else steps[-1]
        