'''
3934-smallest-unique-subarray
'''

from typing import List
from collections import Counter


class Solution:
  def smallestUniqueSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    l, r = 1, n
    b = 215215
    mod = (1<<31) - 1

    # rolling hash and check there should be at least
    # 1 array that has only 1 hash in the counter
    def check(mid: int) -> bool:
      h, p = 0, 1
      for i in range(mid):
        h = (h*b + nums[i]) % mod
        p = (p*b) % mod

      c = Counter([h])
      for i in range(mid, n):
        h = (h*b + nums[i] - nums[i-mid]*p) % mod
        c[h] += 1

      return 1 in c.values()

    while l <= r:
      mid = (l+r) // 2

      if check(mid):
        # mid is a possible len, reduce to find
        # the min
        r = mid-1
      else:
        l = mid+1

    return l
        