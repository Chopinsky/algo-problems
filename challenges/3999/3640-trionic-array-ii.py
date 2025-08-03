'''
3640-trionic-array-ii
'''

from typing import List
import math


class Solution:
  def maxSumTrionic(self, nums: List[int]) -> int:
    n = len(nums)
    res = -math.inf
    prefix = nums[0]
    l = 0
    p = 0
    q = 0

    for r in range(1, n):
      prefix += nums[r]

      # reset
      if nums[r-1] == nums[r]:
        l = r
        prefix = nums[r]
        continue

      if nums[r-1] > nums[r]:
        # flip
        if r > 1 and nums[r-2] < nums[r-1]:
          p = r-1
          while l < q:
            prefix -= nums[l]
            l += 1

          while l+1 < p and nums[l] < 0:
            prefix -= nums[l]
            l += 1

        continue

      if r > 1 and nums[r-2] > nums[r-1]:
        q = r-1

      if l < p and p < q:
        res = max(res, prefix)

    return res

