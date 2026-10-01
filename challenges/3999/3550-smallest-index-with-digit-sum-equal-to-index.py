'''
3550-smallest-index-with-digit-sum-equal-to-index
'''

from typing import List


class Solution:
  def smallestIndex(self, nums: List[int]) -> int:
    for i, val in enumerate(nums):
      s = sum(int(ch) for ch in str(val))
      if s == i:
        return i

    return -1
        