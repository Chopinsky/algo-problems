'''
3621-number-of-integers-with-popcount-depth-equal-to-k-i
'''

from functools import cache


class Solution:
  def popcountDepth(self, n: int, k: int) -> int:
    if k == 0:
      return 1

    cand = set()
    nums = bin(n)[2:]

    def compute(val: int) -> int:
      depth = 0
      while val > 1:
        val = bin(val)[2:].count('1')
        depth += 1

      return depth

    @cache
    def dp(i: int, one: int, tt: bool) -> int:
      if i >= len(nums):
        return 1 if one in cand else 0

      digit = int(nums[i]) if tt else 1
      ans = 0

      for d in range(digit+1):
        nxt_tt = tt and d == digit
        ans += dp(i+1, one+d, nxt_tt)

      return ans

    for val in range(1, 65):
      if compute(val) == k-1:
        cand.add(val)

    if not cand:
      return 0

    count = dp(0, 0, True)
    if k == 1 and 1 in cand:
      return count-1

    return count
