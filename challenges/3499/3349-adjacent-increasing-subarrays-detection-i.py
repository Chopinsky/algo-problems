'''
3349-adjacent-increasing-subarrays-detection-i
'''

from typing import List


class Solution:
  def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
    prev = 0
    curr = 1
    n = len(nums)

    for i in range(1, n):
      if nums[i] <= nums[i-1]:
        prev = curr
        curr = 1
      else:
        curr += 1

      if curr >= 2*k or (curr >= k and prev >= k):
        return True

    return False
        