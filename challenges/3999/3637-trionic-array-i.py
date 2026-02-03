'''
3637-trionic-array-i
'''

from typing import List


class Solution:
  def isTrionic(self, nums: List[int]) -> bool:
    n = len(nums)
    if n <= 3:
      return False

    if any(nums[i] == nums[i-1] for i in range(1, n)):
      return False

    if nums[0] >= nums[1]:
      return False

    ups = 1
    downs = 0
    is_up = True

    for i in range(2, n):
      if is_up:
        if nums[i] < nums[i-1]:
          downs += 1
          is_up = False

      else:
        if nums[i] > nums[i-1]:
          ups += 1
          is_up = True

      if ups > 2 or downs > 1:
        return False

    return ups == 2 and downs == 1

        