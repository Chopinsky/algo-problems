'''
3727-maximum-alternating-sum-of-squares
'''

from typing import List


class Solution:
  def maxAlternatingSum(self, nums: List[int]) -> int:
    n = len(nums)
    nums.sort(key=lambda x: abs(x))
    mid = n//2
    s1 = sum(nums[i]**2 for i in range(mid, n))
    s2 = sum(nums[i]**2 for i in range(mid))

    return s1 - s2
        