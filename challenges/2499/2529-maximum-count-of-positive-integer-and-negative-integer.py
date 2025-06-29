'''
2529-maximum-count-of-positive-integer-and-negative-integer
'''

from typing import List
from bisect import bisect_left, bisect_right


class Solution:
  def maximumCount(self, nums: List[int]) -> int:
    n = len(nums)
    r = bisect_right(nums, 0)
    l = bisect_left(nums, 0)-1 

    return max(n-r, l+1)
        