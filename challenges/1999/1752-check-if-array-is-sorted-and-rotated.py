'''
1752-check-if-array-is-sorted-and-rotated
'''

from typing import List


class Solution:
  def check(self, nums: List[int]) -> bool:
    n = len(nums)
    nums += nums
    s = 0

    for i in range(1, len(nums)):
      val = nums[i]
      if val < nums[i-1]:
        s = i
        continue

      # print('iter:', (i, val), s)
      if i-s+1 >= n:
        return True

    return False
        