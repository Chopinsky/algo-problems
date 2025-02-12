'''
3151 Special Array I
'''

from typing import List


class Solution:
  def isArraySpecial(self, nums: List[int]) -> bool:
    n = len(nums)
    if n <= 1:
      return True

    if nums[0]%2 == nums[1]%2:
      return False

    return all(nums[i]%2 == nums[0 if i%2 == 0 else 1]%2 for i in range(n))

        