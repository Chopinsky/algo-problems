'''
3627-maximum-median-sum-of-subsequences-of-size-3
'''

from typing import List


class Solution:
  def maximumMedianSum(self, nums: List[int]) -> int:
    n = len(nums)
    nums.sort()
    # print('init:', nums)
    l, r = 0, n-1
    s = 0

    while l < r:
      s += nums[r-1]
      r -= 2
      l += 1

    return s

