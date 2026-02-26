'''
3379-transformed-array
'''

from typing import List


class Solution:
  def constructTransformedArray(self, nums: List[int]) -> List[int]:
    n = len(nums)

    def calc_val(i: int) -> int:
      if nums[i] == 0:
        return 0

      j = (i + nums[i]) % n
      return nums[j]

    return [calc_val(i) for i in range(n)]
        