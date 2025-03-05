'''
3265-count-almost-equal-pairs-i
'''

from typing import List
from collections import defaultdict


class Solution:
  def countPairs(self, nums: List[int]) -> int:
    count = defaultdict(int)
    total = 0

    def is_almost_match(v0: int, v1: int):
      if v0 > v1:
        v0, v1 = v1, v0

      a0 = list(str(v0))
      a1 = list(str(v1))
      n0, n1 = len(a0), len(a1)
      
      if n0 < n1:
        a0 = ['0']*(n1-n0) + a0

      i, j = 0, n1-1
      while i < j and a0[i] == a1[i]:
        i += 1

      while i < j and a0[j] == a1[j]:
        j -= 1

      if i > j:
        return True

      if i != j:
        a0[i], a0[j] = a0[j], a0[i]

      return all(a0[i] == a1[i] for i in range(n1))

    nums.sort()
    for i in range(1, len(nums)):
      for j in range(i):
        if is_almost_match(nums[j], nums[i]):
          total += 1

    return total
        