'''
3487-maximum-unique-subarray-sum-after-deletion
'''

from typing import List


class Solution:
  def maxSum(self, nums: List[int]) -> int:
    if max(nums)<0 :
      return max(nums)

    result = 0
    nums = set(nums)
    
    for val in nums:
      if val >= 0:
        result += val

    return result

  def maxSum0(self, nums: List[int]) -> int:
    n = len(nums)
    best = max(nums)
    seen = set()

    for i in range(n):
      seen.clear()
      curr = 0
      for j in range(i, n):
        if nums[j] < 0 or nums[j] in seen:
          continue

        seen.add(nums[j])
        curr += nums[j]
        best = max(best, curr)

    return best
        