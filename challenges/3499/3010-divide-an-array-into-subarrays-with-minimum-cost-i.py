'''
3010-divide-an-array-into-subarrays-with-minimum-cost-i
'''

from typing import List


class Solution:
  def minimumCost(self, nums: List[int]) -> int:
    vals = sorted(nums[1:])
    return nums[0] + sum(vals[:2])
        