'''
3523-make-array-non-decreasing
'''

from typing import List


class Solution:
  def maximumPossibleSize(self, nums: List[int]) -> int:
    res = []

    for val in nums:
      if not res or val >= res[-1]:
        res.append(val)

    return len(res)
