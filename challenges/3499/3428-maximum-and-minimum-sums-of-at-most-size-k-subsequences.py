'''
3428-maximum-and-minimum-sums-of-at-most-size-k-subsequences
'''

from typing import List
from math import comb


class Solution:
  def minMaxSums(self, nums: List[int], k: int) -> int:
    mod = 10**9+7
    if k == 1:
      return (2*sum(nums)) % mod

    nums.sort()
    total = 0
    n = len(nums)
    count = 1

    for i in range(n):
      total += count*(nums[i] + nums[-i-1])
      count = 2*count - comb(i, k-1)

    return total % mod

        