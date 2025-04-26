'''
2873-maximum-value-of-an-ordered-triplet-i
'''

from typing import List


class Solution:
  def maximumTripletValue(self, nums: List[int]) -> int:
    prev = [nums[0]-nums[1], nums[0]-nums[1]]
    n = len(nums)
    max_val = 0

    for i in range(2, n):
      val = nums[i]
      max_val = max(max_val, prev[0]*val, prev[1]*val)
      # print('iter:', val, prev)
      for j in range(i):
        prev[0] = max(prev[0], nums[j]-val)
        prev[1] = min(prev[1], nums[j]-val)

    return max_val
