'''
3655-xor-after-range-multiplication-queries-ii
'''

from typing import List
from math import isqrt
from collections import defaultdict


class Solution:
  def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
    mod = 10**9 + 7
    n = len(nums)
    upper = isqrt(n) + 1
    events = defaultdict(lambda: [1]*n)

    for l, r, k, v in queries:
      if k <= upper:
        events[k][l] = (events[k][l] * v) % mod
        r2 = r + ((l - r) % k or k)
        # print('q:', r2)
        if r2 < n:
          # inverse -- prefix-product reset after this
          events[k][r2] = (events[k][r2] * pow(v, mod-2, mod)) % mod

      else:
        for i in range(l, r+1, k):
          nums[i] = (nums[i] * v) % mod

    for k, multi in events.items():
      # sequentially apply events on all (index, k_step) pairs
      for i in range(k):
        curr = 1
        for j in range(i, n, k):
          # update curr to all multiplies applied at j
          curr = (curr * multi[j]) % mod
          nums[j] = (nums[j] * curr) % mod

    ans = 0
    for val in nums:
      ans ^= val

    return ans

        