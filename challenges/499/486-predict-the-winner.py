'''
486-predict-the-winner
'''

from functools import cache
from typing import List


class Solution:
  def predictTheWinner(self, nums: List[int]) -> bool:
    @cache
    def dp(l: int, r: int):
      if l == r:
        return (nums[l], 0)

      if l+1 == r:
        return (max(nums[l], nums[r]), min(nums[l], nums[r]))

      # take left
      b0, a0 = dp(l+1, r)
      a0 += nums[l]
      d0 = a0 - b0

      # take right
      b1, a1 = dp(l, r-1)
      a1 += nums[r]
      d1 = a1 - b1

      return (a0, b0) if d0 >= d1 else (a1, b1)

    v0, v1 = dp(0, len(nums)-1)
    # print('done:', v0, v1)

    return v0 >= v1
        