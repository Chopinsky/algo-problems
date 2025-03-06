'''
3105-longest-strictly-increasing-or-strictly-decreasing-subarray
'''

from typing import List


class Solution:
  def longestMonotonicSubarray(self, nums: List[int]) -> int:
    s0, s1 = 0, 0
    l0, l1 = 1, 1
    n = len(nums)

    for i in range(1, n):
      if nums[i] > nums[i-1]:
        l0 = max(l0, i-s0+1)
      else:
        s0 = i

      if nums[i] < nums[i-1]:
        l1 = max(l1, i-s1+1)
      else:
        s1 = i

    l0 = max(l0, n-s0)
    l1 = max(l1, n-s1)

    return max(l0, l1)
        