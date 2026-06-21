'''
2784-check-if-array-is-good
'''

from typing import List


class Solution:
  def isGood(self, nums: List[int]) -> bool:
    n = len(nums)
    if n <= 1:
      return False

    nums.sort()
    if nums[-1] != nums[-2] or nums[-1] != n-1:
      return False

    if nums[0] != 1:
      return False

    return all(nums[i-1]+1 == nums[i] for i in range(1, n-1))
        