'''
3574-maximize-subarray-gcd-score
'''

from math import inf, gcd
from typing import List


class Solution:
  def maxGCDScore(self, nums: List[int], k: int) -> int:
    res = max(nums)
    n = len(nums)
    base = []

    for i in range(n):
      low = nums[i] & -nums[i]
      nums[i] //= low
      base.append(low)

    for i in range(n):
      val = nums[i]
      count = 0
      min_pow = inf

      for j in range(i, n):
        val = gcd(val, nums[j])
        if min_pow > base[j]:
          min_pow = base[j]
          count = 0

        if min_pow == base[j]:
          count += 1

        curr = val * min_pow * (2 if count <= k else 1) * (j-i+1)
        res = max(res, curr)

    return res
        