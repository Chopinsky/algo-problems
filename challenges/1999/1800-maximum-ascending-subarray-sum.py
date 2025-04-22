'''
1800-maximum-ascending-subarray-sum
'''

from typing import List


class Solution:
  def maxAscendingSum(self, nums: List[int]) -> int:
    curr = 0
    prev = -1
    res = nums[0]

    for val in nums:
      if val > prev:
        curr += val
      else:
        curr = val

      res = max(res, curr)
      prev = val

    return res
