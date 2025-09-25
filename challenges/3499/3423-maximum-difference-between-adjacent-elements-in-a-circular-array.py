'''
3423-maximum-difference-between-adjacent-elements-in-a-circular-array
'''

from typing import List


class Solution:
  def maxAdjacentDistance(self, nums: List[int]) -> int:
    n = len(nums)
    d0 = abs(nums[-1] - nums[0])
    d1 = max(abs(nums[i+1]-nums[i]) for i in range(n-1))
    return max(d0, d1)
        