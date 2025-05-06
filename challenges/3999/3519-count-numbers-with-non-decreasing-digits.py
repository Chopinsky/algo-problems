'''
3519-count-numbers-with-non-decreasing-digits
'''

from functools import cache


class Solution:
  def countNumbers(self, l: str, r: str, b: int) -> int:
    mod = 10**9 + 7

    def convert(val: str):
      val = int(val)
      if val == 0:
        return '0'

      result = ""
      while val > 0:
        result = str(val % b) + result
        val //= b

      return result

    l = convert(str(int(l)-1))
    r = convert(r)
    # print('init:', l, r)

    @cache
    def dp(num: str, idx: int, is_upper: bool, prev: int):
      if idx == len(num):
        return 1

      curr = int(num[idx])
      l = curr+1 if is_upper else b
      ans = 0

      for d in range(prev, l):
        ans += dp(num, idx+1, is_upper and curr == d, d)

      return ans % mod

    return (dp(r, 0, True, 0) - dp(l, 0, True, 0)) % mod
        