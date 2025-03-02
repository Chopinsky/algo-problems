'''
2460-apply-operations-to-an-array
'''

from typing import List


class Solution:
  def applyOperations(self, nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n):
      if i < n-1 and nums[i] == nums[i+1]:
        nums[i] *= 2
        nums[i+1] = 0

    res = [val for val in nums if val != 0]
    res += [0]*(n-len(res))

    return res
        