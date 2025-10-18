'''
3551-minimum-swaps-to-sort-by-digit-sum
'''

from functools import cache
from typing import List


class Solution:
  def minSwaps(self, nums: List[int]) -> int:
    @cache
    def sort_value(val: int) -> int:
      res = 0
      while val > 0:
        res += val%10
        val //= 10

      return res

    target = sorted(nums, key=lambda x: (sort_value(x), x))
    ops = 0
    pos = {val: idx for idx, val in enumerate(target)}
    seen = set()
    # print('init:', pos, target)

    for i in range(len(nums)):
      if i in seen:
        continue

      action = False
      while i not in seen:
        seen.add(i)
        val = nums[i]
        if pos[val] == i:
          break

        # swap into this position
        i = pos[val]
        ops += 1
        action = True

      if action:
        ops -= 1

    return ops
        