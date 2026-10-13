'''
3689-maximum-total-subarray-value-i
'''

from typing import List


class Solution:
  def maxTotalValue(self, nums: List[int], k: int) -> int:
    lo = min(nums)
    hi = max(nums)
    return k*(hi-lo)
