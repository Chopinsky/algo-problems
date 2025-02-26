'''
3355-zero-array-transformation-i
'''

from typing import List
from collections import defaultdict


class Solution:
  def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
    changes = defaultdict(int)
    delta = 0
    n = len(nums)

    for l, r in queries:
      changes[l] -= 1
      changes[r+1] += 1

    for i in range(n):
      if i in changes:
        delta += changes[i]

      if nums[i] + delta > 0:
        return False

    return True
