'''
3649-number-of-perfect-pairs
'''

from typing import List


class Solution:
  def perfectPairs(self, nums: List[int]) -> int:
    a = sorted(abs(val) for val in nums)
    cnt = 0
    j = 0
    n = len(a)

    for i in range(len(nums)):
      while j < n and a[j] <= 2*a[i]:
        j += 1

      cnt += max(0, j-i-1)

    return cnt
        