'''
3966-count-good-integers-in-a-range
'''

from functools import cache


class Solution:
  def goodIntegers(self, l: int, r: int, k: int) -> int:
    def count(val: int) -> int:
      s = list(int(d) for d in str(val))

      @cache
      def iter(i: int, prev: int, tight: bool, started: bool) -> int:
        if i >= len(s):
          return 1 if started else 0

        upper = s[i] if tight else 9
        ans = 0

        for d in range(upper+1):
          if not started and d == 0:
            # not started
            ans += iter(i+1, -1, tight and d == upper, False)
            continue

          if not started or abs(prev - d) <= k:
            # satarting/started and can use d here
            ans += iter(i+1, d, tight and d == upper, True)

        return ans
      
      return iter(0, -1, True, False)

    return count(r) - count(l-1)
        