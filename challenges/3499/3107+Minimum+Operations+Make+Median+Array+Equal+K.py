'''
3107. Minimum Operations to Make Median of Array Equal to K
'''

from typing import List

class Solution:
  def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
    n = len(nums)
    if n == 1:
      return abs(nums[0] - k)
    
    nums.sort()

    mid = n//2
    ops = 0
    
    if nums[mid] == k:
      return ops
    
    l = mid
    while l >= 0 and nums[l] > k:
      ops += abs(nums[l] - k)
      l -= 1
      
    r = mid
    while r < n and nums[r] < k:
      ops += abs(nums[r] - k)
      r += 1
      
    return ops
        