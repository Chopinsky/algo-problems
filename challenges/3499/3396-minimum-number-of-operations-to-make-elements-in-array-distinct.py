'''
3396-minimum-number-of-operations-to-make-elements-in-array-distinct
'''

from typing import List
from collections import Counter


class Solution:
  def minimumOperations(self, nums: List[int]) -> int:
    c = Counter(nums)
    cand = set([val for val in c if c[val] > 1])
    # print('init:', c, cand)
    if not cand:
      return 0

    def update(i: int):
      if i >= len(nums):
        return

      val = nums[i]
      c[val] -= 1
      if c[val] < 2:
        cand.discard(val)

    ops = 0
    for i in range(0, len(nums), 3):
      update(i)
      update(i+1)
      update(i+2)
      ops += 1

      if not cand:
        break

    return ops
        