from typing import List
from itertools import combinations
from functools import lru_cache
from shared.mm import gcd


class Solution:
  def maxScore(self, nums: List[int], k: int) -> int:
    @lru_cache
    def dp(src: List[int], kval: int) -> int:
      if len(src) == 0:
        return 0

      val = 0
      for (a, b) in combinations(src):
        next_arr = filter(lambda x: x != a and x != b, src)
        val = max(val, kval * gcd(a, b) + dp(next_arr, kval+1))

      return val

    return dp(nums, k)
