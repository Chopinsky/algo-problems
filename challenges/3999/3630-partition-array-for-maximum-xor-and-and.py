'''
3630-partition-array-for-maximum-xor-and-and
'''

from typing import List


class Solution:
  def maximizeXorAndXor(self, nums: List[int]) -> int:
    n = len(nums)
    total = 0
    for val in nums:
      total ^= val

    def get_basis(arr: List) -> List:
      basis = []
      for val in arr:
        for b in basis:
          val = min(val, val^b)

        if val:
          basis.append(val)

      return basis

    def get_max_xor(basis: List) -> int:
      max_xor = 0
      for b in basis:
        max_xor = max(max_xor, max_xor^b)

      return max_xor

    res = 0
    for mask in range(1, 1<<n):
      and_set = -1
      xor_set = 0
      unselected = []

      for i in range(n):
        if (mask>>i) & 1:
          xor_set ^= nums[i]
          if and_set == -1:
            and_set = nums[i]
          else:
            and_set &= nums[i]

        else:
          unselected.append(nums[i])

      unselected_xor = total ^ xor_set
      inverted = ~unselected_xor

      reduced = [(x & inverted) for x in unselected]
      basis = get_basis(reduced)
      max_xor = get_max_xor(basis)

      res = max(res, and_set + unselected_xor + 2*max_xor)

    return res
        