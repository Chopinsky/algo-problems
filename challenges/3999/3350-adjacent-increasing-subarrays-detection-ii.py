'''
3350-adjacent-increasing-subarrays-detection-ii
'''

from typing import List


class Solution:
  def maxIncreasingSubarrays(self, nums: List[int]) -> int:
    ln = 1
    prev = 0
    n = len(nums)
    ans = 1

    for i in range(1, n):
      if nums[i] > nums[i-1]:
        ln += 1
      else:
        prev = ln
        ln = 1

      ans = max(
        ans,
        ln // 2,
        min(prev, ln)
      )

    return ans
