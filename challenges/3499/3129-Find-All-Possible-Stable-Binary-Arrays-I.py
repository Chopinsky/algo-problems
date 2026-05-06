'''
3129-Find-All-Possible-Stable-Binary-Arrays-I
'''

from functools import cache


class Solution:
  def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
    mod = 10**9 + 7

    @cache
    def count(a: int, b: int) -> int:
      if a == 0:
        return 0

      if b == 0:
        return a <= limit

      # gen [1, upper] count of a
      upper = min(a, limit)
      a -= 1
      total = 0

      for more_a in range(upper):
        total += count(b, a-more_a)

      return total % mod

    c0 = count(zero, one)
    c1 = count(one, zero)

    return (c0 + c1) % mod
        