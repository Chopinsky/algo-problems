'''
3566-partition-array-into-two-equal-product-subsets
'''

from typing import List


class Solution:
  def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
    n = len(nums)

    def test(i: int, p1: int, p2: int) -> bool:
      if i >= n:
        return p1 == target and p2 == target

      if p1 > target or p2 > target:
        return False

      val = nums[i]

      return test(i+1, p1*val, p2) or test(i+1, p1, p2*val)

    return test(0, 1, 1)