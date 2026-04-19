'''
3906-count-good-integers-on-a-grid-path
'''

from functools import cache


class Solution:
  def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
    i = 0
    pth = set([i])

    for d in directions:
      i += 4 if d == 'D' else 1
      pth.add(i)

    def cnt(s: int):
      s = str(s).zfill(16)

      @cache
      def dp(i: int, prev: int, tight: bool) -> int:
        if i >= len(s):
          return 1

        res, limit = 0, int(s[i]) if tight else 9

        for d in range(limit+1):
          # on the path
          if i in pth:
            # need non-decreasing value
            if d >= prev:
              res += dp(i+1, d, tight and d==limit)

          else:
            # all other digits, only need to be under the 
            # upper bound -- limit
            res += dp(i+1, prev, tight and d==limit)

        return res

      return dp(0, 0, True)

    return cnt(r) - cnt(l-1)
        