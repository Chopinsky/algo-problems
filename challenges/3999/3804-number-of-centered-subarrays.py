'''
3804-number-of-centered-subarrays
'''

from typing import List


class Solution:
  def centeredSubarrays(self, nums: List[int]) -> int:
    n = len(nums)

    def count(i: int) -> int:
      curr = 0
      seen = set()
      cnt = 0

      for j in range(i, n):
        curr += nums[j]
        seen.add(nums[j])

        if curr in seen:
          cnt += 1

      return cnt

    return sum(count(i) for i in range(n))
