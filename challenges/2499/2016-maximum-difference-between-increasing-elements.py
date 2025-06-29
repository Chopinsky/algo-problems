'''
2016-maximum-difference-between-increasing-elements
'''

from typing import List


class Solution:
  def maximumDifference(self, nums: List[int]) -> int:
    res = -1
    prev = float('inf')

    for val in nums:
      if val > prev:
        res = max(res, val - prev)
      
      prev = min(prev, val)

    return res
        