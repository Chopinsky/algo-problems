'''
3587-minimum-adjacent-swaps-to-alternate-parity
'''

from typing import List


class Solution:
  def minSwaps(self, nums: List[int]) -> int:
    n = len(nums)
    odd = [i for i in range(n) if nums[i]%2 == 1]
    even = [i for i in range(n) if nums[i]%2 == 0]
    lo = len(odd)
    le = len(even)
    # print('init:', odd, even)

    if abs(lo-le) > 1:
      return -1

    def into_positions(cand: List) -> int:
      target = [i for i in range(0, n, 2)]
      if len(target) != len(cand):
        return -1

      ops = 0
      for i in range(len(target)):
        ops += abs(target[i] - cand[i])

      return ops

    if lo == le:
      return min(
        into_positions(odd),
        into_positions(even),
      )

    return into_positions(odd) if lo > le else into_positions(even)
