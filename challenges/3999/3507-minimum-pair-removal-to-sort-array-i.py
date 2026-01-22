'''
3507-minimum-pair-removal-to-sort-array-i
'''

from typing import List

import math


class Solution:
  def minimumPairRemoval(self, nums: List[int]) -> int:
    def find() -> int:
      n = len(nums)
      idx = -1
      val = math.inf

      for i in range(n-1):
        v0 = nums[i]+nums[i+1]
        if v0 < val:
          idx = i
          val = v0

      return idx

    def check() -> bool:
      n = len(nums)
      return all(nums[i] <= nums[i+1] for i in range(n-1))

    ops = 0

    while not check():
      idx = find()
      nums = nums[:idx] + [nums[idx]+nums[idx+1]] + nums[idx+2:]
      ops += 1
      # print('iter:', ops, nums)

    return ops

        