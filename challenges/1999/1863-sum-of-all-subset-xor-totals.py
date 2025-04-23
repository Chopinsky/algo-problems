'''
1863-sum-of-all-subset-xor-totals
'''

from typing import List


class Solution:
  def subsetXORSum(self, nums: List[int]) -> int:
    curr = 0
    n = len(nums)

    for val in range(1, (1<<n)):
      # print('iter:', bin(val)[2:])
      base = 0
      for i in range(n):
        if (1<<i) & val > 0:
          base ^= nums[i]

      curr += base

    return curr
        