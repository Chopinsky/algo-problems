'''
3300-minimum-element-after-replacement-with-digit-sum
'''

from typing import List


class Solution:
  def minElement(self, nums: List[int]) -> int:
    def convert(val: int) -> int:
      s = 0
      while val > 0:
        s += val % 10
        val //= 10

      # print('done:', s)
      return s

    return min(convert(val) for val in nums)
        