'''
3634-minimum-removals-to-balance-array
'''

from typing import List


class Solution:
  def minRemoval(self, nums: List[int], k: int) -> int:
    nums.sort()
    j = 0
    n = len(nums)
    ops = n-1

    for i in range(n):
      if j >= n:
        break

      while j < n and nums[j] <= k*nums[i]:
        j += 1

      sz = j-i
      ops = min(ops, n-sz)

    return ops
