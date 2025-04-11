'''
3375-minimum-operations-to-make-array-values-equal-to-k
'''

from typing import List


class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    if any(val < k for val in nums):
      return -1

    vals = sorted(set(nums))
    n = len(vals)
    # print('init:', vals, n)
    return n if k < vals[0] else n-1
